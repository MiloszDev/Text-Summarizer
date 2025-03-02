import os
import sys
import zipfile

sys.path.insert(0, r'D:\Projects\Text-Summarization\src')

import pytest
from unittest.mock import patch, MagicMock
from src.entities.models import DataIngestionConfig
from src.components.data_ingestion import DataIngestion


@pytest.fixture
def config():
    return DataIngestionConfig(
        source_url="http://example.com/data.zip",
        data_file="data.zip",
        unzip_dir="unzip_dir"
    )

@patch("urllib.request.urlretrieve")
def test_download_data(mock_urlretrieve, config):
    mock_urlretrieve.return_value = None
    ingestion = DataIngestion(config)
    
    ingestion.download_data()

    mock_urlretrieve.assert_called_once_with(config.source_url, config.data_file)

@patch("urllib.request.urlretrieve")
def test_download_data_already_exists(mock_urlretrieve, config):
    os.makedirs(config.unzip_dir, exist_ok=True)
    with open(config.data_file, "w") as f:
        f.write("dummy content")
    
    ingestion = DataIngestion(config)
    ingestion.download_data()

    mock_urlretrieve.assert_not_called()

@patch("zipfile.ZipFile")
def test_extract_file(mock_zipfile, config):
    mock_zipfile.return_value.__enter__.return_value.extractall = MagicMock()

    ingestion = DataIngestion(config)
    ingestion.extract_file()

    mock_zipfile.return_value.__enter__.return_value.extractall.assert_called_once_with(config.unzip_dir)

@patch("zipfile.ZipFile")
def test_extract_file_bad_zip(mock_zipfile, config):
    mock_zipfile.side_effect = zipfile.BadZipFile("Bad zip file")

    ingestion = DataIngestion(config)

    with pytest.raises(zipfile.BadZipFile):
        ingestion.extract_file()