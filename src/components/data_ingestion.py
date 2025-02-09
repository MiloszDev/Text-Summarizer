"""Module for ingesting data: downloading and extracting files from a URL."""

import os
import zipfile
import urllib.request as request

from logger.handlers import logger
from entities.models import DataIngestionConfig

class DataIngestion:
    """
    Manages downloading and extracting data.
    """
    
    def __init__(self, config: DataIngestionConfig) -> None:
        """
        Initializes with configuration for data ingestion.
        """
        self.config = config

    def download_data(self) -> None:
        """
        Downloads the file if it doesn't already exist.
        """
        if not os.path.exists(self.config.data_file):
            try:
                request.urlretrieve(self.config.source_url, self.config.data_file)
                logger.info(f"Downloaded file: {self.config.data_file}")
            
            except Exception as e:
                logger.error(f"Download failed: {e}")
                raise

        else:
            logger.info(f"File already exists: {self.config.data_file}")

    def extract_file(self):
        """
        Extracts the zip file to the specified directory.
        """
        os.makedirs(self.config.unzip_dir, exist_ok=True)

        try:
            with zipfile.ZipFile(self.config.data_file, 'r') as zip_ref:
                zip_ref.extractall(self.config.unzip_dir)
                logger.info(f"Extracted to: {self.config.unzip_dir}")

        except (zipfile.BadZipFile, Exception) as e:
            logger.error(f"Extraction failed: {e}")
            raise