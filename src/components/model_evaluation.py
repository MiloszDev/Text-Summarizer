import torch

from evaluate import load
from src.logger.handlers import logger
from src.entities.models import ModelEvaluationConfig
from transformers import T5ForConditionalGeneration, T5Tokenizer


class ModelEvaluation:
    """
    A class to handle the evaluation of a text summarization model.
    """

    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.model = T5ForConditionalGeneration.from_pretrained(
            self.config.model_path
        ).to(self.device)
        self.tokenizer = T5Tokenizer.from_pretrained(self.config.tokenizer_path)

        self.metric = load(self.config.evaluation_metric)

    def summarize_text(self, text):
        input_ids = self.tokenizer.encode(
            "summarize: " + text,
            return_tensors="pt",
            max_length=512,
            truncation=True,
        )
        input_ids = input_ids.to(self.device)

        summary_ids = self.model.generate(
            input_ids,
            max_length=128,
            min_length=50,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True,
        )

        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return summary

    def calculate_metric(self, predictions, references):
        return self.metric.compute(predictions=predictions, references=references)

    def evaluate_model(self, samples):
        input_ids = samples["input_ids"]
        labels = samples["labels"]

        print(input_ids, type(input_ids))
        print(labels, type(labels))

        predictions = [
            self.summarize_text(
                self.tokenizer.decode(input_id, skip_special_tokens=True)
            )
            for input_id in input_ids
        ]

        labels = [
            self.tokenizer.decode(label, skip_special_tokens=True) for label in labels
        ]

        results = self.calculate_metric(predictions, labels)

        logger.info(f"Evaluation results: {results}")

        return results
