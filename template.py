import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

files = [
    '.github/workflows/deployment_pipeline_config.yaml',
    
    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_preprocessing.py',
    'src/components/model_training.py',
    'src/components/model_evaluation.py',
    'src/utils/__init__.py',
    'src/utils/functions.py',
    'src/logger/__init__.py',
    'src/logger/handlers.py',
    'src/config/__init__.py',
    'src/config/settings.py',
    'src/stages/__init__.py',
    'src/stages/data_ingestion.py',
    'src/stages/data_preprocessing.py',
    'src/stages/model_training_stage.py',
    'src/stages/model_evaluation_stage.py',
    'src/stages/Prediction.py',
    'src/entities/__init__.py',
    'src/entities/models.py',
    'src/settings/__init__.py',
    'src/settings/constants.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'docs/README.md',
    'research/experiments.ipynb',
    'tests/integration/test.py',
    'test/unit/test.py'
]

for filepath in files:
    path = Path(filepath)
    directory = path.parent

    try:
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {directory}")
        else:
            logging.info(f"Directory already exists: {directory}")

        if not path.exists():
            with open(path, 'w') as f:
                logging.info(f"Created file: {path}")
        else:
            logging.info(f"File already exists: {path}")

    except Exception as e:
        logging.error(f"Error creating {filepath}: {e}")
