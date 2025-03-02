"""Defines configuration models for the various data pipeline stages."""

from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration for data ingestion.
    """
    datasets: list

@dataclass(frozen=True)
class DataPreprocessingConfig:
    """
    Configuration for data preprocessing.
    """
    model_name: str
    inputs_max_length: int
    labels_max_length: int

@dataclass(frozen=True)
class ModelTrainingConfig:
    """
    Configuration for model training.
    """
    model_name: str
    eval_strategy: str
    learning_rate: float
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    num_train_epochs: int
    weight_decay: float
    logging_dir: Path
    logging_steps: int
    save_strategy: str
    report_to: str
    output_dir: Path

@dataclass(frozen=True)
class ModelEvaluationConfig:
    model_path: str
    tokenizer_path: str
    evaluation_metric: str