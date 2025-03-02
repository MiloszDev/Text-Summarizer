"""Orchestrates the data ingestion process, including downloading and extracting data."""

import pandas as pd

from typing import Tuple
from src.logger.handlers import logger
from src.config.settings import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    """
    Manages the data ingestion pipeline: loading config, downloading, and extracting data.
    """

    def __init__(self):
        """
        Initializes the pipeline.
        """
        pass

    def run(self, eval_dataset):
        """
        Runs the data ingestion process.
        """
        config_manager = ConfigurationManager()

        evaluation_config = config_manager.get_model_evaluation_config()

        evaluation_handler = ModelEvaluation(config=evaluation_config)

        return evaluation_handler.evaluate_model(eval_dataset)