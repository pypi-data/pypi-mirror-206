import os
from .dataset import DataSet
from ._timeslice import Timeslice
from ._tables import Tables, _INDEX_WILDCARD
from ._stage_type import StageType
from .dataset import dataset_factory
from ._utils import abs_config_path, load_yaml, get_config_path, check_version
from ._logging_config import configure_logging


class Config:
    _TABLES = "tables"
    _CONFIG_PATH = "config_path"

    def __init__(self, pattern: str, config_path: str = None):
        configure_logging()

        self.config = self._load_config(pattern, config_path)
        self.tables = self._load_tables()

    def _load_config(self, pattern: str, config_path: str):
        config_path = get_config_path(config_path)
        config_file = f"{pattern}.yaml"

        config_file_path = os.path.join(config_path, config_file)
        config = load_yaml(config_file_path)
        check_version(config)

        # add the configuration path into the confif dictionart
        # so that it gets passed to table config when created
        config[self._CONFIG_PATH] = config_path
        return config

    def _load_tables(self):
        tables_path = self.config[self._TABLES]
        tables_path = abs_config_path(
            self.config[self._CONFIG_PATH], self.config[self._TABLES]
        )

        data = load_yaml(tables_path)
        check_version(data)
        self.config[self._TABLES] = data

        tables = Tables(
            table_data=self.config[self._TABLES],
            config_path=self.config[self._CONFIG_PATH],
        )
        return tables

    def get_table_mapping(
        self,
        timeslice: Timeslice,
        stage: StageType,
        table: str = _INDEX_WILDCARD,
        database: str = _INDEX_WILDCARD,
    ):
        table_mapping = self.tables.get_table_mapping(
            stage=stage, table=table, database=database
        )

        table_mapping.source = dataset_factory.get_data_set(
            self.config, table_mapping.source, timeslice
        )
        table_mapping.destination = dataset_factory.get_data_set(
            self.config, table_mapping.destination, timeslice
        )

        return table_mapping

    def set_checkpoint(
        self,
        source: DataSet,
        destination: DataSet,
        checkpoint_name: str = None,
    ):
        if not checkpoint_name:
            checkpoint_name = f"{source.database}.{source.table}-{destination.database}.{destination.table}"

        source.checkpoint = checkpoint_name
        source._render()
        destination.checkpoint = checkpoint_name
        destination.options["checkpointLocation"] = destination.checkpoint_location
        destination._render()
