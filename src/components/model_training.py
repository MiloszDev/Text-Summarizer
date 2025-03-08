import torch
from transformers import TrainingArguments, Trainer
from transformers import T5Tokenizer, T5ForConditionalGeneration
from src.entities.models import ModelTrainingConfig


class ModelTraining:
    """
    Manages the model training process.
    """

    def __init__(self, config: ModelTrainingConfig) -> None:
        """
        Initializes with configuration for model training.
        """
        self.config = config

    def train_model(self, train_data, test_data, save_model=False):
        device = "cuda" if torch.cuda.is_available() else "cpu"

        tokenizer = T5Tokenizer.from_pretrained(self.config.model_name)
        model = T5ForConditionalGeneration.from_pretrained(self.config.model_name).to(
            device
        )

        training_args = TrainingArguments(
            output_dir=self.config.output_dir,
            evaluation_strategy=self.config.eval_strategy,
            learning_rate=self.config.learning_rate,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            num_train_epochs=self.config.num_train_epochs,
            weight_decay=self.config.weight_decay,
            logging_dir=self.config.logging_dir,
            logging_steps=self.config.logging_steps,
            save_strategy=self.config.save_strategy,
            report_to=self.config.report_to,
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_data,
            eval_dataset=test_data,
            tokenizer=tokenizer,
        )

        trainer.train()

        if save_model:
            model.save_pretrained(self.config.output_dir)
            tokenizer.save_pretrained(self.config.output_dir)

        return model, tokenizer
