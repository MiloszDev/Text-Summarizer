# import pytest
# from unittest import mock
# from src.components.model_training import ModelTraining
# from transformers import T5ForConditionalGeneration, Trainer

# @pytest.fixture
# def mock_train_data():
#     return mock.MagicMock()

# @pytest.fixture
# def mock_test_data():
#     return mock.MagicMock()

# @pytest.fixture
# def mock_config():
#     return mock.MagicMock()

# @pytest.fixture
# def mock_train():
#     return mock.MagicMock()

# @mock.patch("transformers.T5ForConditionalGeneration.from_pretrained")
# @mock.patch("transformers.Trainer.train")
# def test_device_selection(mock_train, mock_from_pretrained, mock_config, mock_train_data, mock_test_data):
#     model_training = ModelTraining(config=mock_config)
#     model, tokenizer = model_training.train_model(mock_train_data, mock_test_data, save_model=False)
#     assert model is not None
#     assert tokenizer is not None

# @mock.patch("transformers.Trainer.train")
# def test_train_model_without_saving(mock_train, mock_config, mock_train_data, mock_test_data):
#     model_training = ModelTraining(config=mock_config)
#     model, tokenizer = model_training.train_model(mock_train_data, mock_test_data, save_model=False)
#     assert model is not None
#     assert tokenizer is not None

# @mock.patch("transformers.T5ForConditionalGeneration.save_pretrained")
# @mock.patch("transformers.T5Tokenizer.save_pretrained")
# @mock.patch("transformers.Trainer.train")
# def test_train_model_with_saving(mock_save_tokenizer, mock_save_model, mock_train, mock_config, mock_train_data, mock_test_data):
#     model_training = ModelTraining(config=mock_config)
#     model, tokenizer = model_training.train_model(mock_train_data, mock_test_data, save_model=True)
#     assert model is not None
#     assert tokenizer is not None
