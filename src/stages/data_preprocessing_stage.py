"""Orchestrates the data ingestion process, including downloading and extracting data."""

import pandas as pd

from typing import Tuple
from src.logger.handlers import logger
from src.config.settings import ConfigurationManager
from src.components.data_preprocessing import DataPreprocessing

class DataPreprocessingPipeline:
    """
    Manages the data ingestion pipeline: loading config, downloading, and extracting data.
    """

    def __init__(self):
        """
        Initializes the pipeline.
        """
        pass

    def run(self, train_data, test_data) -> Tuple[pd.DataFrame]:
        """
        Runs the data ingestion process.
        """
        config_manager = ConfigurationManager()

        preprocessing_config = config_manager.get_data_preprocessing_config()

        preprocessing_handler = DataPreprocessing(config=preprocessing_config)

        return preprocessing_handler.preprocess_data(train_data, test_data)