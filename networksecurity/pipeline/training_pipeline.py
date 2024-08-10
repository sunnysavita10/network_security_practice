import sys
import os

#importing components
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.components.model_evaluation import ModelEvaluation
from networksecurity.components.model_pusher import ModelPusher

#importing exception and logging module
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import NetworkSecurityLogger

#importing configuration entity
from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    ModelPusherConfig
)

#importing artifact entity
from networksecurity.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
    ModelEvaluationArtifact,
    ModelPusherArtifact
)



class TrainingPipeline:
    is_pipeline_running = False
    def __init__(self):
        pass
    
    def start_data_ingestion(self):
        """_summary_
        """
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) 
    
    def start_data_validation(self):
        """_summary_
        """
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_data_transformation(self):
        """_summary_
        """
        try:
            pass
        except Exception as e:
            pass
        
    def model_training(self):
        """_summary_
        """
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def model_evaluation(self):
        """_summary_
        """
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def model_pusher(self):
        """_summary_
        """
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def run_pipeline(self):
        try:
            TrainingPipeline.is_pipeline_running = True
            
            self.start_data_ingestion()
            self.start_data_validation()
            self.start_data_transformation()
            self.model_training()
            self.model_evaluation()
            self.model_pusher()
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)