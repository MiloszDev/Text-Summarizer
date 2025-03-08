"""Orchestrates the data ingestion process, including downloading and extracting data."""

from src.config.settings import ConfigurationManager
from src.components.data_ingestion import DataIngestion


class DataIngestionPipeline:
    """
    Manages the data ingestion pipeline: loading config, downloading, and extracting data.
    """

    def __init__(self):
        """
        Initializes the pipeline.
        """
        pass

    def run(self) -> None:
        """
        Runs the data ingestion process.
        """
        config_manager = ConfigurationManager()

        ingestion_config = config_manager.get_data_ingestion_config()

        ingestion_handler = DataIngestion(config=ingestion_config)

        ingestion_handler.download_data()
        ingestion_handler.extract_file()
