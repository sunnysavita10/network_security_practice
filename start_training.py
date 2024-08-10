import sys
import os

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.pipeline.training_pipeline import TrainingPipeline

def start_training():
    
    """
    this method runs a training pipeline.
    """
    
    try:
        model_training=TrainingPipeline()
        model_training.run_pipeline()
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
    
    
if __name__ == '__main__':
    start_training()
    