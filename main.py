import os
import sys
import logging
import pandas as pd

from src.logger.handlers import logger
from src.stages.data_ingestion_stage import DataIngestionPipeline
from src.stages.data_preprocessing_stage import DataPreprocessingPipeline
from src.stages.model_training_stage import ModelTrainingPipeline
from src.stages.model_evaluation_stage import ModelEvaluationPipeline

def run_data_ingestion(STAGE_NAME="Data Ingestion"):
    """
    Executes the data ingestion pipeline, logging the start and completion status.
    """
    try:
        logger.info(f"Stage '{STAGE_NAME}' started.")
        
        ingestion_pipeline = DataIngestionPipeline()
        train_data, test_data = ingestion_pipeline.run()
        
        logger.info(f"Stage '{STAGE_NAME}' completed successfully.")
        
        return train_data, test_data

    except Exception as e:
        logger.exception(f"Stage '{STAGE_NAME}' failed: {e}")
        raise e

def run_data_preprocessing(train_data, test_data, STAGE_NAME="Data Preprocessing"):
    """
    Executes the data preprocessing pipeline, logging the start and completion status.
    """
    try:
        logger.info(f"Stage '{STAGE_NAME}' started.")
        
        preprocessing_pipeline = DataPreprocessingPipeline()
        tokenized_train, tokenized_test = preprocessing_pipeline.run(train_data, test_data)
        
        logger.info(f"Stage '{STAGE_NAME}' completed successfully.")
        
        return tokenized_train, tokenized_test
    
    except Exception as e:
        logger.exception(f"Stage '{STAGE_NAME}' failed: {e}")
        raise e

def run_model_training(tokenized_train, tokenized_test, STAGE_NAME="Model Training"):
    """
    Executes the model training pipeline, logging the start and completion status.
    """
    try:
        logger.info(f"Stage '{STAGE_NAME}' started.")
                
        training_pipeline = ModelTrainingPipeline()
        model, tokenizer = training_pipeline.run(tokenized_train, tokenized_test)
                
        logger.info(f"Stage '{STAGE_NAME}' completed successfully.")
                
        return model, tokenizer
            
    except Exception as e:
        logger.exception(f"Stage '{STAGE_NAME}' failed: {e}")
        raise e

def run_model_evaluation(eval_dataset, STAGE_NAME="Model Evaluation"):
    """
    Executes the model evaluation pipeline, logging the start and completion status.
    """
    try:
        logger.info(f"Stage '{STAGE_NAME}' started.")
                
        evaluation_pipeline = ModelEvaluationPipeline()
        results = evaluation_pipeline.run(eval_dataset)
        
        logger.info(f"Stage '{STAGE_NAME}' completed successfully.")
        
        return results
    
    except Exception as e:
        logger.exception(f"Stage '{STAGE_NAME}' failed: {e}")
        raise e

if __name__ == "__main__":
    train_data, test_data = run_data_ingestion()
    
    tokenized_train, tokenized_test = run_data_preprocessing(train_data, test_data)
    
    model, tokenizer = run_model_training(tokenized_train, tokenized_test)
    
    results = run_model_evaluation(pd.DataFrame(list(tokenized_test)[:5]))
    logger.info(f"Evaluation Results: {results}")