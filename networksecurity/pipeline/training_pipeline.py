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
from networksecurity.logger.logger import logging

#importing configuration entity
from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    ModelPusherConfig,
    TrainingPipelineConfig
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
        self.training_pipeline_config = TrainingPipelineConfig()
        
    
    def start_data_ingestion(self):
        """_summary_
        """
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
            
        except Exception as e:
            raise NetworkSecurityException(e, sys) 
    
    def start_data_validaton(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config = data_validation_config
            )
            data_validation_artifact = data_validation.initiate_data_validation()
            return data_validation_artifact
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
            
            data_ingestion_artifact:DataIngestionArtifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validaton(data_ingestion_artifact=data_ingestion_artifact)
            #self.start_data_transformation()
            #self.model_training()
            #self.model_evaluation()
            #self.model_pusher()
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)
