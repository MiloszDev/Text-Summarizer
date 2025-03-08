import pytest
from unittest.mock import MagicMock, patch
from datasets import Dataset
from src.entities.models import DataPreprocessingConfig
from src.components.data_preprocessing import DataPreprocessing


@pytest.fixture
def mock_config():
    return DataPreprocessingConfig(
        model_name='t5-small',
        inputs_max_length=512,
        labels_max_length=128
    )


@pytest.fixture
def mock_data():
    data = {
        'dialogue': ["Hello", "How are you?"],
        'summary': ["Greeting", "Question"]
    }
    train_data = Dataset.from_dict(data)
    test_data = Dataset.from_dict(data)
    return train_data, test_data


@patch("transformers.T5Tokenizer.from_pretrained")
def test_preprocess_function(mock_tokenizer, mock_config, mock_data):
    train_data, _ = mock_data
    preprocessing = DataPreprocessing(mock_config)

    mock_tokenizer_instance = MagicMock()
    mock_tokenizer.return_value = mock_tokenizer_instance
    mock_tokenizer_instance.return_value = {
        'input_ids': [[101, 102], [103, 104]],
        'attention_mask': [[1, 1], [1, 1]]
    }

    result = preprocessing.preprocess_function(train_data)

    assert 'input_ids' in result
    assert 'attention_mask' in result
    assert 'labels' in result
    assert len(result['input_ids']) == len(train_data)
    assert len(result['attention_mask']) == len(train_data)
    assert result['input_ids'] == [[101, 102], [103, 104]]
    assert result['attention_mask'] == [[1, 1], [1, 1]]


@patch("transformers.T5Tokenizer.from_pretrained")
def test_preprocess_function_empty_input(mock_tokenizer, mock_config):
    data = {'dialogue': [], 'summary': []}
    train_data = Dataset.from_dict(data)
    
    preprocessing = DataPreprocessing(mock_config)
    mock_tokenizer_instance = MagicMock()
    mock_tokenizer.return_value = mock_tokenizer_instance
    mock_tokenizer_instance.return_value = {
        'input_ids': [],
        'attention_mask': []
    }

    result = preprocessing.preprocess_function(train_data)

    assert result['input_ids'] == []
    assert result['attention_mask'] == []


@patch("transformers.T5Tokenizer.from_pretrained")
def test_preprocess_function_with_different_config(mock_tokenizer, mock_data):
    mock_config_small = DataPreprocessingConfig(
        model_name='t5-small',
        inputs_max_length=10,
        labels_max_length=5
    )
    train_data, _ = mock_data
    preprocessing = DataPreprocessing(mock_config_small)

    mock_tokenizer_instance = MagicMock()
    mock_tokenizer.return_value = mock_tokenizer_instance
    mock_tokenizer_instance.return_value = {
        'input_ids': [[101, 102]],
        'attention_mask': [[1, 1]]
    }

    result = preprocessing.preprocess_function(train_data)

    assert len(result['input_ids'][0]) <= mock_config_small.inputs_max_length
    assert len(result['attention_mask'][0]) <= mock_config_small.inputs_max_length


@patch("transformers.T5Tokenizer.from_pretrained")
def test_preprocess_function_tokenization_failure(mock_tokenizer, mock_data):
    mock_tokenizer.side_effect = Exception("Tokenization failed")

    data = {'dialogue': ["Hello", "How are you?"], 'summary': ["Greeting", "Question"]}
    train_data = Dataset.from_dict(data)

    mock_config = DataPreprocessingConfig(
        model_name='t5-small',
        inputs_max_length=512,
        labels_max_length=128
    )

    preprocessing = DataPreprocessing(mock_config)

    with pytest.raises(Exception, match="Tokenization failed"):
        preprocessing.preprocess_function(train_data)


@patch("transformers.T5Tokenizer.from_pretrained")
def test_tokenizer_called_with_correct_model(mock_tokenizer, mock_config, mock_data):
    train_data, _ = mock_data
    preprocessing = DataPreprocessing(mock_config)

    mock_tokenizer_instance = MagicMock()
    mock_tokenizer.return_value = mock_tokenizer_instance
    mock_tokenizer_instance.return_value = {
        'input_ids': [[101, 102]],
        'attention_mask': [[1, 1]]
    }

    preprocessing.preprocess_function(train_data)

    mock_tokenizer.assert_called_with(mock_config.model_name)
