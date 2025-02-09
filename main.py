import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from logger.handlers import logger  # type: ignore
from stages.data_ingestion_stage import DataIngestionPipeline  # type: ignore

STAGE_NAME = "Data Ingestion"

def run_data_ingestion():
    """
    Executes the data ingestion pipeline, logging the start and completion status.
    """
    try:
        logger.info(f"Stage '{STAGE_NAME}' started.")
        
        ingestion_pipeline = DataIngestionPipeline()
        ingestion_pipeline.run()
        
        logger.info(f"Stage '{STAGE_NAME}' completed successfully.")
        
    except Exception as e:
        logger.exception(f"Stage '{STAGE_NAME}' failed: {e}")
        raise e

if __name__ == "__main__":
    run_data_ingestion()
