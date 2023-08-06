# implicit, not referenced - must be the 1st import
from ._logging_config import configure_logging, YETL_CONFIG
import logging
from ._config import Config
from ._timeslice import Timeslice
from ._stage_type import StageType
import os


def yetl_flow(stage: StageType, config_path: str = None, pattern: str = None):
    def decorate(function):
        def wrap_function(*args, **kwargs):
            configure_logging()
            _logger = logging.getLogger(__name__)

            _pattern = pattern
            if not _pattern:
                _pattern = function.__name__

            _logger.info(f"Loading pipeline configuration {_pattern}")

            _config_path = config_path
            if not config_path:
                _config_path = os.getenv(YETL_CONFIG, "../config")

            timeslice = kwargs.get("timeslice", Timeslice(day="*", month="*", year="*"))
            if "timeslice" in kwargs.keys():
                del kwargs["timeslice"]

            try:
                table = kwargs["table"]
                del kwargs["table"]
            except KeyError as e:
                raise Exception(f"{e} is a required argument for a yetl flow function")

            config = Config(pattern=_pattern, config_path=_config_path)
            table_mapping = config.get_table_mapping(
                timeslice=timeslice, stage=stage, table=table
            )
            _logger.info(f"Calling function {function.__name__}")
            ret = function(
                *args,
                table_mapping=table_mapping,
                **kwargs,
            )
            return ret

        return wrap_function

    return decorate
