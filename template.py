import os
import logging

from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

files = [
    ".github/workflows/.gitkeep",
    
    "src/__init__.py",

    "src/components/__init__.py",

    "src/utils/__init__.py",
    "src/utils/functions.py",

    'src/logger/__init__.py',
    'src/logger/handlers.py',

    'src/config/__init__.py',
    'src/config/settings.py',

    'src/stages/__init__.py',
    'src/stages/data_ingestion.py',
    'src/stages/data_preprocessing.py',
    'src/stages/trainer.py',
    'src/stages/evaluation.py',

    'src/entities/__init__.py',
    "src/entities/models.py",

    'src/settings/__init__.py',
    'src/settings/params.py'

    "config/config.yaml",
    "params.yaml",

    "app.py",
    "main.py",

    "Dockerfile",
    "requirements.txt",
    "setup.py",

    "research/experiments.ipynb",

    "tests/test.py"
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