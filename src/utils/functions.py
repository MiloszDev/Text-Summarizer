import os
import yaml

from pathlib import Path
from box import ConfigBox
from typing import List, Union
from logger.handlers import logger
from ensure import ensure_annotations
from box.exceptions import BoxValueError # type: ignore

@ensure_annotations
def read_yaml(path_to_yaml_file: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml_file: Path to the YAML file.

    Returns:
        ConfigBox: The content of the YAML file in a ConfigBox format.
    """
    try:
        with open(path_to_yaml_file, "r") as file:
            content = yaml.safe_load(file)
            logger.info(f"Successfully read YAML file: {path_to_yaml_file}")
            return ConfigBox(content)

    except BoxValueError as e:
        logger.error(f"Box error while reading YAML file: {path_to_yaml_file}")
        raise e

    except Exception as e:
        logger.error(f"Unexpected error while reading YAML file: {path_to_yaml_file} - {str(e)}")
        raise e

def create_directories(path_to_directories: List[Union[str, Path]], verbose: bool = True) -> None:
    """
    Create a list of directories.

    Args:
        path_to_directories: List of directories to create.
        verbose: Whether to print logs or not.
    """
    for path in path_to_directories:
        path = Path(path)
        
        try:
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)
                if verbose:
                    logger.info(f"Created directory: {path}")
            else:
                if verbose:
                    logger.info(f"Directory already exists: {path}")

        except Exception as e:
            logger.error(f"Error creating {path}: {e}")


@ensure_annotations
def get_file_size(path: Path) -> str:
    """
    Get the size of a file in KB.

    Args:
        path: Path to the file.
    
    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    
    return f"~ {size_in_kb} KB"