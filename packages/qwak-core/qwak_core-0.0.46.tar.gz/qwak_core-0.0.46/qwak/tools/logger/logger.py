import logging
import logging.config
import os
from pathlib import Path

import yaml
from qwak.exceptions import QwakException

DEFAULT_LOGGER_NAME = "qwak"
REMOTE_LOGGER_NAME = "qwak_remote"
MODEL_LOGGER_NAME = "qwak_model"
FEATURE_STORE_LOGGER_NAME = "feature_store"
BUILD_LOCAL_LOGGER_NAME = "build_local"
DOCKER_INTERNAL_LOGGER_NAME = "docker_internal"

ENVIRON_LOGGER_TYPE = "LOGGER_TYPE"

BUILD_LOCAL_FILE_HANDLER_NAME = "build_log_file_handler"
FILE_HANDLER_NAME = "file_handler"
CONSOLE_HANDLER_NAME = "console"
REMOTE_CONSOLE_HANDLER_NAME = "remote_console"

DEFINED_LOGGER_NAMES = {
    DEFAULT_LOGGER_NAME,
    REMOTE_LOGGER_NAME,
    MODEL_LOGGER_NAME,
    FEATURE_STORE_LOGGER_NAME,
    BUILD_LOCAL_LOGGER_NAME,
    DOCKER_INTERNAL_LOGGER_NAME,
}

VERBOSITY_LEVEL_MAPPING = {0: logging.CRITICAL, 1: logging.INFO, 2: logging.DEBUG}
REVERSED_VERBOSITY_LEVEL_MAPPING = {
    value: key for key, value in VERBOSITY_LEVEL_MAPPING.items()
}

AIRFLOW_ENV_FLAG = "AIRFLOW__LOGGING__REMOTE_LOGGING"
LOGGING_CONFIG_FILE_NAME = "logging.yml"
HANDLERS_KEY = "handlers"
FILE_HANDLER_KEY = "file_handler"
FILE_NAME = "filename"
DISABLE_EXISTING_LOGGERS_KEY = "disable_existing_loggers"
LOGFILE_DEFAULT_NAME = "qwak.log"

LOGGER_CONFIGURATION_EXCEPTION_MESSAGE = (
    "Error in Logging Configuration. Error message: {e}"
)
LOGGER_NOT_FOUND_MESSAGE = (
    "Failed to get requested logger name {logger_name}. Using default logger"
)
ANOTHER_LOGGER_FOUND_MESSAGE = (
    "Another logger is already enabled, not changing configuration"
)
LOGGER_HANDLER_ADDITION_NOT_FOUND_MESSAGE = (
    "Tried to set orphan loggers handlers with a non-existing logger name handlers"
)
DEFAULT_LOGGER_PATH = Path.home() / ".qwak" / "log" / LOGFILE_DEFAULT_NAME


def setup_qwak_logger(
    logs_folder: str = None,
    log_file_name: str = LOGFILE_DEFAULT_NAME,
    logger_name_handler_addition: str = None,
    disable_existing_loggers: bool = False,
):
    """Setup qwak logger:
            1. Rotating file in $HOME/.qwak/log/sdk.log (10MB * 5 files) (DEBUG level)
            2. Stdout logger with colored logs. (INFO level)

    Args:
        logs_folder: Folder where logs will be stored
        log_file_name: The name of the log file. Default: qwak.log
        logger_name_handler_addition:
            Logger name which the handlers of will be appended to all loggers which have handlers
            Overriding stdout stream handler if exists
        disable_existing_loggers: disables all existing loggers

    Raises:
        QwakException: If loading logging.yml fails or the preparation of the logging environment raises an exception

    Notes:
        1. https://docs.python.org/3/library/logging.html#logging-levels
    """

    logs_folder = logs_folder if logs_folder else DEFAULT_LOGGER_PATH
    config_file = Path(__file__).parent / LOGGING_CONFIG_FILE_NAME
    if not non_qwak_logger_enabled():
        # Creating log directory
        log_path = _create_logs_path(logs_folder)
        _load_config(log_file_name, config_file, disable_existing_loggers, log_path)
        logger = get_qwak_logger()

        if logger_name_handler_addition:
            if logger_name_handler_addition in logging.Logger.manager.loggerDict:
                _add_logger_handlers(logger_name_handler_addition)
            else:
                logger.warning(LOGGER_HANDLER_ADDITION_NOT_FOUND_MESSAGE)

    else:
        logger = logging.getLogger(__file__)
        logger.info(ANOTHER_LOGGER_FOUND_MESSAGE)


def _create_logs_path(logs_folder: str) -> Path:
    log_path = Path(logs_folder)
    log_path.mkdir(parents=True, exist_ok=True)
    return log_path


def _load_config(
    log_file_name: str,
    config_file: Path,
    disable_existing_loggers: bool,
    log_path: Path,
) -> None:
    with config_file.open(mode="rt") as f:
        try:
            # Load logger configuration
            config = yaml.safe_load(f.read())
            config[HANDLERS_KEY][FILE_HANDLER_KEY][FILE_NAME] = str(
                log_path / log_file_name
            )
            config[DISABLE_EXISTING_LOGGERS_KEY] = disable_existing_loggers

            logging.config.dictConfig(config)

        except Exception as e:
            raise QwakException(LOGGER_CONFIGURATION_EXCEPTION_MESSAGE.format(e=e))


def _add_logger_handlers(logger_name: str) -> None:
    """
    Add a specific logger handlers to all loggers
    Override loggers StreamHandler handlers if the input logger has a StreamHandler

    Args:
        logger_name: logger name which consists of the handlers we wish to set
    """

    requested_logger_handlers = logging.getLogger(logger_name).handlers
    replace_stdout_handler = any(
        [
            handler
            for handler in requested_logger_handlers
            if isinstance(handler, logging.StreamHandler)
        ]
    )

    for existing_logger in [
        logger
        for logger in logging.Logger.manager.loggerDict.values()
        if not isinstance(logger, logging.PlaceHolder)
    ]:
        if existing_logger.handlers:
            if replace_stdout_handler:
                existing_handlers = list(
                    filter(
                        lambda h: not isinstance(h, logging.StreamHandler),
                        existing_logger.handlers,
                    )
                )
            else:
                existing_handlers = existing_logger.handlers
            existing_logger.handlers = existing_handlers + requested_logger_handlers


def get_qwak_logger() -> logging.Logger:
    """Get qwak logger (Singleton)

    Returns:
        logging.Logger: Qwak logger.
    """
    logger_name = get_qwak_logger_name()

    if (logger_name not in DEFINED_LOGGER_NAMES) and not non_qwak_logger_enabled():
        print(LOGGER_NOT_FOUND_MESSAGE.format(logger_name=logger_name))

    return logging.getLogger(logger_name)


def get_qwak_logger_name() -> str:
    return os.getenv(ENVIRON_LOGGER_TYPE, DEFAULT_LOGGER_NAME)


def non_qwak_logger_enabled() -> bool:
    return os.getenv(AIRFLOW_ENV_FLAG) is not None
