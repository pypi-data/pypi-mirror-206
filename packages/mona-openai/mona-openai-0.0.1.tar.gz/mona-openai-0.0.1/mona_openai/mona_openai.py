import time
import asyncio
from copy import deepcopy
from types import MappingProxyType

from mona_sdk import MonaSingleMessage

from .exceptions import WrongOpenAIClassException
from .mona_client import get_mona_clients
from .util.func_util import (
    add_conditional_sampling,
    call_non_blocking_sync_or_async,
)
from .endpoints.completion import (
    COMPLETION_CLASS_NAME,
    get_completion_class,
    get_analysis_params as completion_analysis_getter,
    get_clean_message as completion_message_cleaner,
)
from .util.validation_util import validate_and_get_sampling_ratio

EMPTY_DICT = MappingProxyType({})

MONA_ARGS_PREFIX = "MONA_"
CONTEXT_ID_ARG_NAME = MONA_ARGS_PREFIX + "context_id"
EXPORT_TIMESTAMP_ARG_NAME = MONA_ARGS_PREFIX + "export_timestamp"
ADDITIONAL_DATA_ARG_NAME = MONA_ARGS_PREFIX + "additional_data"

# TODO(Itai): This is essetially a nice-looking "switch" statement. We should
#   try to use the name to find the exact monitoring-enrichment function and
#   filename instead of listing all options here.
ENDPOINT_NAME_TO_WRAPPER = {COMPLETION_CLASS_NAME: get_completion_class}


def _get_monitored_base_class(openai_class):
    """
    Returns a class that wrapps the given api class with that
    api-specific functionality.
    """
    class_name = openai_class.__name__

    if class_name not in ENDPOINT_NAME_TO_WRAPPER:
        raise WrongOpenAIClassException("Class not supported: " + class_name)
    return ENDPOINT_NAME_TO_WRAPPER[class_name](openai_class)


def _get_mona_single_message(
    api_name,
    request_input,
    start_time,
    is_exception,
    is_async,
    response,
    analysis_params_getter,
    specs,
    context_class,
    message_cleaner,
    additional_data,
    context_id,
    export_timestamp,
):
    """
    Returns a MonaSingleMessage object to be used for data
    exporting to Mona's servers by a Mona client.
    """

    message = {
        "input": request_input,
        "latency": time.time() - start_time,
        "is_exception": is_exception,
        "api_name": api_name,
        "is_async": is_async,
    }

    if additional_data:
        message["additional_data"] = additional_data

    if response:
        message["response"] = response
        message["analysis"] = analysis_params_getter(
            request_input, response, specs
        )

    message = message_cleaner(message, specs)

    return MonaSingleMessage(
        message=message,
        contextClass=context_class,
        contextId=context_id,
        exportTimestamp=export_timestamp,
    )


# TODO(itai): Consider creating some sturct (as NamedTuple or dataclass) for
#   the specs param.


def monitor(
    openai_class,
    mona_creds,
    context_class,
    specs=EMPTY_DICT,
    mona_clients_getter=get_mona_clients,
):
    """
    Returns a Wrapped version of a given OpenAI class with mona
    monitoring logic.
    This is the main exposed function of the mona_openai package and
    probably the only thing you need to use from this package.

    You can use the returned class' "create" and "acreate" functions
    exactly as you would the original class, and monitoring will be
    taken care of for you.

    This client will automatically monitor for you things like latency,
    prompt and response lengths, number of tokens, etc., along with any
    endpoint parameter usage (e.g., it tracks the "temperature" and
    "max_tokens" params you use).

    You can also add other named args when calling "create" or
    "acreate" by using a new named argument called
    "MONA_additional_data" and set it to any JSON serializable
    dictionary.
    This allows you to add metadata about the call such as a prompt
    template ID, information about the context in which the API call is
    made, etc...

    Furthermore, you can add to create/acreate functions mona specific
    arguments:
        MONA_context_id: The unique id of the context in which the call
            is made. By using this ID you can export more data to Mona
            to the same context from other places. If not used, the
            "id" field of the OpenAI Endpoint's response will be used.
        MONA_export_timestamp: Can be used to simulate as if the
            current call was made in a different time, as far as Mona
            is concerned.

    The returned monitored class also exposes a new class method called
    "get_mona_clients", which allows you to retrieve the clients and
    use them to export more data or communicate directly with Mona's
    API

    Read more about Mona and how to use it in Mona's docs on
    https://docs.monalabs.io.

    Args:
        openai_class: An OpenAI API class to wrap with monitoring
            capabilties.
        mona_creds: Either a dict or pair of Mona API key and secret to
            set up Mona's clients from its SDK
        context_class: The Mona context class name to use for
            monitoring. Use a name of your choice.
        specs: A dictionary of specifications such as monitoring
            sampling ratio.
        mona_clients_getter: Used only for testing purposes
    """
    client, async_client = mona_clients_getter(mona_creds)

    sampling_ratio = validate_and_get_sampling_ratio(specs)

    base_class = _get_monitored_base_class(openai_class)

    # TODO(itai): Add call to Mona servers to init the context class if it
    #   isn't inited yet once we have the relevant endpoint for this.

    class MonitoredOpenAI(base_class):
        """
        A mona-monitored version of an openai API class.
        """

        @classmethod
        def _get_mona_single_message(
            cls, kwargs_param, start_time, is_exception, is_async, response
        ):
            """
            Returns a MonaSingleMessage object to be used for data
            exporting to Mona's servers by a Mona client.
            """
            # Recreate the input dict to avoid manipulating the caller's data,
            # and remove Mona-related data.
            request_input = deepcopy(
                {
                    x: kwargs_param[x]
                    for x in kwargs_param
                    if not x.startswith(MONA_ARGS_PREFIX)
                }
            )

            return _get_mona_single_message(
                api_name=openai_class.__name__,
                request_input=request_input,
                start_time=start_time,
                is_exception=is_exception,
                is_async=is_async,
                response=response,
                analysis_params_getter=super()._get_analysis_params,
                specs=specs,
                context_class=context_class,
                message_cleaner=super()._get_clean_message,
                additional_data=kwargs_param.get(ADDITIONAL_DATA_ARG_NAME),
                context_id=kwargs_param.get(
                    CONTEXT_ID_ARG_NAME, response["id"] if response else None
                ),
                export_timestamp=kwargs_param.get(
                    EXPORT_TIMESTAMP_ARG_NAME, start_time
                ),
            )

        @classmethod
        async def _inner_create(
            cls, export_function, super_function, args, kwargs
        ):
            """
            The main logic for wrapping create functions with mona data
            exporting.
            This internal function porovides a template for both sync
            and async activations (helps with wrapping both "create"
            and "acreate").
            """
            start_time = time.time()

            response = None

            async def _inner_mona_export(is_exception):
                return await call_non_blocking_sync_or_async(
                    export_function,
                    (
                        cls._get_mona_single_message(
                            kwargs,
                            start_time,
                            is_exception,
                            super_function.__name__ == "acreate",
                            response,
                        ),
                    ),
                )

            mona_export = add_conditional_sampling(
                _inner_mona_export, sampling_ratio
            )

            try:
                # Call the actual openai create function without the Mona
                # specific arguments.
                response = await call_non_blocking_sync_or_async(
                    super_function,
                    args,
                    {
                        x: kwargs[x]
                        for x in kwargs
                        if not x.startswith(MONA_ARGS_PREFIX)
                    },
                )
            except Exception:
                if not specs.get("avoid_monitoring_exceptions", False):
                    await mona_export(True)
                raise

            await mona_export(False)

            return response

        @classmethod
        def create(cls, *args, **kwargs):
            """
            A mona-monitored version of the openai base class' "create"
            function.
            """
            return asyncio.run(
                cls._inner_create(client.export, super().create, args, kwargs)
            )

        @classmethod
        async def acreate(cls, *args, **kwargs):
            """
            An async mona-monitored version of the openai base class'
            "acreate" function.
            """
            return await cls._inner_create(
                async_client.export_async, super().acreate, args, kwargs
            )

        @classmethod
        def get_mona_clients(cls):
            """
            Returns the two Mona clients this class works with to allow
            exporting more data or communicating directly with Mona's
            API.
            """
            return (client, async_client)

    return type(base_class.__name__, (MonitoredOpenAI,), {})


def get_rest_monitor(
    openai_endpoint_name,
    mona_creds,
    context_class,
    specs=EMPTY_DICT,
    mona_clients_getter=get_mona_clients,
):
    """
    Returns a client class for monitoring OpenAI REST calls not done
    using the OpenAI python client (e.g., for Azure users using their
    endpoints directly). This isn't a wrapper for any http requesting
    library and doesn't call the OpenAI API for you - it's just an easy
    logging client to log requests, responses and exceptions.
    """

    # TODO(itai): Consider creating an async version as well.
    client, _ = mona_clients_getter(mona_creds)

    sampling_ratio = validate_and_get_sampling_ratio(specs)

    class RestClient:
        """
        This will be the returned Mona logging class. We follow
        OpenAI's way of doing things by using a static classe with
        relevant class methods.
        """

        @classmethod
        def log_request(
            cls,
            request_dict,
            additional_data=None,
            context_id=None,
            export_timestamp=None,
        ):
            """
            This function should be called with a request data dict,
            for example, what you would use as "json" when using
            "requests" to post.

            It returns a response logging function to be used with the
            response object.
            """
            start_time = time.time()

            inner_response = None

            def _inner_mona_export(is_exception):
                return client.export(
                    _get_mona_single_message(
                        api_name=openai_endpoint_name,
                        request_input=request_dict,
                        start_time=start_time,
                        is_exception=is_exception,
                        is_async=False,
                        response=inner_response,
                        analysis_params_getter=completion_analysis_getter,
                        specs=specs,
                        context_class=context_class,
                        message_cleaner=completion_message_cleaner,
                        additional_data=additional_data,
                        context_id=context_id,
                        export_timestamp=export_timestamp,
                    )
                )

            mona_export = add_conditional_sampling(
                _inner_mona_export, sampling_ratio
            )

            def log_response(response):
                """
                Only when this function is called, will data be logged
                out to Mona. This function should be called with a
                response object from the OpenAI API as close as
                possible to when it is received to allow accurate
                latency logging.
                """
                nonlocal inner_response
                inner_response = response
                return mona_export(False)

            def log_exception():
                return mona_export(True)

            return log_response, log_exception

        @classmethod
        def get_mona_client(cls):
            """
            Returns the two Mona client this class works with to allow
            exporting more data or communicating directly with Mona's
            API.
            """
            return client

    return RestClient
