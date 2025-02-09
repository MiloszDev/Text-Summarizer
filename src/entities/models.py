"""Defines configuration models for the various data pipeline stages."""

from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration for data ingestion.
    """
    root_dir: Path
    unzip_dir: Path
    data_file: Path
    source_url: str