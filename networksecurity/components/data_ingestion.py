#import logging and exception
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
#import train_test split
from sklearn.model_selection import train_test_split
#configuration of component and artifact generation
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
#utility libraries
import os
import sys
import pandas as pd
import numpy as np
from typing import List,Optional
import pymongo

#loading env variable
from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self):
        pass
    
    def export_collection_as_dataframe(
        self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def export_data_into_feature_store(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def split_data_as_train_test(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def initiate_data_ingestion(self):
        try:
            DATABASE_NAME="KNAcd"
            COLLECTION_NAME="NetworkSecurityData"
            dataframe = self.export_collection_as_dataframe(DATABASE_NAME,COLLECTION_NAME)
            dataframe = self.export_data_into_feature_store
            dataframe = dataframe.drop(self._schema_config["drop_columns"],axis=1)
            self.split_data_as_train_test(dataframe=dataframe)
            
            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
            test_file_path=self.data_ingestion_config.testing_file_path)
            return data_ingestion_artifact
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__ == '__main__':
    DATABASE_NAME="KNAcd"
    COLLECTION_NAME="NetworkSecurityData"
    data_ingestion = DataIngestion()
    dataframe = data_ingestion.export_collection_as_dataframe(DATABASE_NAME,COLLECTION_NAME)
    print(dataframe)