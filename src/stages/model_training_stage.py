"""Orchestrates the data ingestion process, including downloading and extracting data."""

from src.config.settings import ConfigurationManager
from src.components.model_training import ModelTraining


class ModelTrainingPipeline:
    """
    Manages the data ingestion pipeline: loading config, downloading, and extracting data.
    """

    def __init__(self):
        """
        Initializes the pipeline.
        """
        pass

    def run(self, train_data, test_data):
        """
        Runs the data ingestion process.
        """
        config_manager = ConfigurationManager()

        training_config = config_manager.get_model_training_config()

        training_handler = ModelTraining(config=training_config)

        return training_handler.train_model(train_data, test_data)
