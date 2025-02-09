"""Manages loading configurations and creating necessary directories for the data pipeline."""

from pathlib import Path
from settings.constants import *
from entities.models import DataIngestionConfig
from utils.functions import read_yaml, create_directories

class ConfigurationManager:
    """
    Loads configuration and parameters, and creates required directories.
    
    Args:
        config_filepath: Path to the configuration file.
        params_filepath: Path to the parameters file.
    """

    def __init__(self, config_filepath: Path = CONFIG_FILE_PATH, params_filepath: Path = PARAMS_FILE_PATH) -> None:
        try:
            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)

            artifacts_root = Path(self.config.artifacts_root)

            create_directories([artifacts_root])

        except Exception as e:
            raise RuntimeError(f"Error loading configuration files or creating directories: {e}")

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Returns data ingestion configuration.
        
        Returns:
            DataIngestionConfig: Configuration for data ingestion.
        """
        try:
            config = self.config.data_ingestion
            create_directories([config.root_dir])

            return DataIngestionConfig(
                root_dir=config.root_dir,
                unzip_dir=config.unzip_dir,
                data_file=config.data_file,
                source_url=config.source_url,
            )
        except Exception as e:
            raise RuntimeError(f"Error getting data ingestion configuration: {e}")
