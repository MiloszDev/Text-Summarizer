"""Module for ingesting data: downloading and extracting files from a URL."""

import os
import zipfile
import urllib.request as request

from typing import Union, Tuple
from src.logger.handlers import logger
from src.entities.models import DataIngestionConfig
from datasets import load_dataset, concatenate_datasets # type: ignore

class DataIngestion:
    """
    Manages downloading and extracting data.
    """
    
    def __init__(self, config: DataIngestionConfig) -> None:
        """
        Initializes with configuration for data ingestion.
        """
        self.config = config

    def rename_columns(self, dataset):
        if "dialogue_act" in dataset.column_names:
            dataset = dataset.rename_column("dialogue_act", "summary")
        return dataset

    def load_datasets(self):
        datasets = []
        for dataset in list(self.config.datasets):
            try:
                datasets.append(load_dataset(dataset, trust_remote_code=True))
                logger.info(f"Loaded dataset: {dataset}")     
                datasets[-1] = self.rename_columns(datasets[-1])
            except Exception as e:
                logger.error(f"Failed to load dataset {dataset}: {e}")
                continue
            
        if datasets:
            train_data = concatenate_datasets([dataset['train'] for dataset in datasets])
            test_data = concatenate_datasets([dataset['test'] for dataset in datasets])

            logger.info(f"Combined dataset: {train_data.num_rows} training samples, {test_data.num_rows} test samples.")
            return train_data, test_data
        else:
            logger.error("No datasets were loaded successfully.")
            return None


