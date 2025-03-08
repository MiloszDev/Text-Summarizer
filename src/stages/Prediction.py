from src.config.settings import ConfigurationManager
from transformers import T5Tokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text):
        tokenizer = T5Tokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {
            'max_length': 128,
            'min_length': 50,
            'length_penalty': 2.0,
            'num_beams': 4,
            'early_stopping': True
        }

        pipe = pipeline('summarization', model=self.config.model_path, tokenizer=tokenizer)

        print(f'Dialogue:\n{text}')

        output = pipe(text, **gen_kwargs)[0]['summary_text']

        print(f'\nModel Summary:\n{output}')

        return output
