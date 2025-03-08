from unittest.mock import patch
from datasets import Dataset, DatasetDict
from src.components.data_ingestion import DataIngestion
from src.entities.models import DataIngestionConfig


@patch("src.components.data_ingestion.load_dataset")
def test_load_datasets(mock_load_dataset):
    mock_train = Dataset.from_dict({"text": ["sample1", "sample2"]})
    mock_test = Dataset.from_dict({"text": ["sample3", "sample4"]})
    mock_dataset = DatasetDict({"train": mock_train, "test": mock_test})

    mock_load_dataset.return_value = mock_dataset

    config = DataIngestionConfig(datasets=["mock_dataset"])
    data_ingestion = DataIngestion(config)
    train_data, test_data = data_ingestion.load_datasets()

    assert train_data is not None
    assert test_data is not None
    assert train_data.num_rows == 2
    assert test_data.num_rows == 2


@patch("src.components.data_ingestion.concatenate_datasets")
@patch("src.components.data_ingestion.load_dataset")
def test_concatenate_datasets(mock_load_dataset, mock_concatenate):
    mock_train = Dataset.from_dict({"text": ["sample1", "sample2"]})
    mock_test = Dataset.from_dict({"text": ["sample3", "sample4"]})
    mock_dataset = DatasetDict({"train": mock_train, "test": mock_test})

    mock_load_dataset.return_value = mock_dataset

    mock_concatenate.side_effect = lambda x: x[0]

    config = DataIngestionConfig(datasets=["mock_dataset"])
    data_ingestion = DataIngestion(config)
    
    train_data, test_data = data_ingestion.load_datasets()

    mock_concatenate.assert_called()
    assert train_data.num_rows == 2
    assert test_data.num_rows == 2


@patch("src.components.data_ingestion.logger")
@patch("src.components.data_ingestion.load_dataset")
def test_logging_behavior(mock_load_dataset, mock_logger):
    mock_train = Dataset.from_dict({"text": ["sample1", "sample2"]})
    mock_test = Dataset.from_dict({"text": ["sample3", "sample4"]})
    mock_dataset = DatasetDict({"train": mock_train, "test": mock_test})

    mock_load_dataset.return_value = mock_dataset

    config = DataIngestionConfig(datasets=["mock_dataset"])
    data_ingestion = DataIngestion(config)

    train_data, test_data = data_ingestion.load_datasets()

    mock_logger.info.assert_any_call("Loaded dataset: mock_dataset")
    mock_logger.info.assert_any_call(
        "Combined dataset: 2 training samples, 2 test samples."
    )

    assert train_data.num_rows == 2
    assert test_data.num_rows == 2


@patch("src.components.data_ingestion.load_dataset")
def test_load_dataset_called_with_correct_arguments(mock_load_dataset):
    mock_train = Dataset.from_dict({"text": ["sample1", "sample2"]})
    mock_test = Dataset.from_dict({"text": ["sample3", "sample4"]})
    mock_dataset = DatasetDict({"train": mock_train, "test": mock_test})

    mock_load_dataset.return_value = mock_dataset

    config = DataIngestionConfig(datasets=["mock_dataset"])
    data_ingestion = DataIngestion(config)
    train_data, test_data = data_ingestion.load_datasets()

    mock_load_dataset.assert_called_with("mock_dataset", trust_remote_code=True)
