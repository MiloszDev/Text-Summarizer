"""Manages loading configurations and creating necessary directories for the data pipeline."""

from pathlib import Path
from src.settings.constants import *
from src.entities.models import (DataIngestionConfig,
                                 DataPreprocessingConfig,
                                 ModelTrainingConfig,
                                 ModelEvaluationConfig)  # Add this import
from src.utils.functions import read_yaml, create_directories

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

            return DataIngestionConfig(
                datasets=config.datasets
            )

        except Exception as e:
            raise RuntimeError(f"Error getting data ingestion configuration: {e}")
    
    def get_data_preprocessing_config(self) -> DataPreprocessingConfig:
        """
        Returns data ingestion configuration.
        
        Returns:
            DataIngestionConfig: Configuration for data ingestion.
        """
        try:
            config = self.config.data_preprocessing

            return DataPreprocessingConfig(
                model_name=config.model_name,
                inputs_max_length=config.inputs_max_length,
                labels_max_length=config.labels_max_length
            )

        except Exception as e:
            raise RuntimeError(f"Error getting data ingestion configuration: {e}")

    def get_model_training_config(self) -> ModelTrainingConfig:
        """
        Returns model training configuration.
        
        Returns:
            ModelTrainingConfig: Configuration for model training.
        """
        try:
            config = self.config.model_training
            params = self.params.TrainingArguments

            return ModelTrainingConfig(
                model_name=config.model_name,
                eval_strategy=params.eval_strategy,
                learning_rate=float(params.learning_rate),
                per_device_train_batch_size=params.per_device_train_batch_size,
                per_device_eval_batch_size=params.per_device_eval_batch_size,
                num_train_epochs=params.num_train_epochs,
                weight_decay=params.weight_decay,
                logging_dir=params.logging_dir,
                logging_steps=params.logging_steps,
                save_strategy=params.save_strategy,
                report_to=params.report_to,
                output_dir=Path(params.output_dir)
            )

        except Exception as e:
            raise RuntimeError(f"Error getting model training configuration: {e}")

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        """
        Returns model evaluation configuration.
        
        Returns:
            ModelEvaluationConfig: Configuration for model evaluation.
        """
        try:
            config = self.config.model_evaluation

            return ModelEvaluationConfig(
                model_path=config.model_path,
                tokenizer_path=config.tokenizer_path,
                evaluation_metric=config.evaluation_metric
            )

        except Exception as e:
            raise RuntimeError(f"Error getting model evaluation configuration: {e}")