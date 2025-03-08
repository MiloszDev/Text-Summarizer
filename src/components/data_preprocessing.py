from transformers import T5Tokenizer
from src.logger.handlers import logger
from src.entities.models import DataPreprocessingConfig


class DataPreprocessing:
    """
    Manages downloading and extracting data.
    """

    def __init__(self, config: DataPreprocessingConfig) -> None:
        """
        Initializes with configuration for data ingestion.
        """
        self.config = config

    def preprocess_function(self, dataset):
        tokenizer = T5Tokenizer.from_pretrained(self.config.model_name)

        inputs = ["summarize: " + str(d) for d in dataset["dialogue"]]
        targets = [str(s) for s in dataset["summary"]]

        model_inputs = tokenizer(
            inputs,
            max_length=self.config.inputs_max_length,
            padding="max_length",
            truncation=True,
        )
        try:
            labels = tokenizer(
                targets,
                max_length=self.config.labels_max_length,
                padding="max_length",
                truncation=True,
            )
        except Exception as e:
            logger.error(f"Error in tokenizing targets: {e}")
            raise

        model_inputs["labels"] = labels["input_ids"]
        return model_inputs

    def preprocess_data(self, train_data, test_data):
        tokenized_train_data = train_data.map(
            self.preprocess_function,
            batched=True,
            remove_columns=train_data.column_names,
        )
        tokenized_test_data = test_data.map(
            self.preprocess_function,
            batched=True,
            remove_columns=test_data.column_names,
        )

        return tokenized_train_data, tokenized_test_data
