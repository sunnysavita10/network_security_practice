import sys
import json
from typing import List, Tuple, Optional
import os

from dotenv import load_dotenv
load_dotenv()
MONGODB_URL=os.getenv("MONGODB_URL")

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json_convertor(self,file_path):
        
        """
        it read the data from the source
        """
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def pushing_data_to_mongodb(self,records,database_name: str,collection_name: str):
        if database_name is not None:
            try:
                
                self.records=records
                self.database_name=database_name
                self.collection_name=collection_name
                
                self.client = pymongo.MongoClient(MONGODB_URL)
                
                self.client.admin.command('ping')
                print("Pinged your deployment. You successfully connected to MongoDB!")
                
                self.database = self.client[self.database_name]
            
                self.collection=self.database[self.collection_name]
                
                self.collection.insert_many(self.records)
                
                return len(self.records)
                
            except Exception as e:
                raise NetworkSecurityException(e, sys)
            
    def export_collection_as_dataframe(
        self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            
            collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__=='__main__':
    DATA_FILE_PATH="./networkdata/network_data.csv"
    DATABASE_NAME="KNAcademy"
    COLLECTION_NAME="NetworkSecurity"
    networkdata=NetworkDataExtract()
    records = networkdata.csv_to_json_convertor(DATA_FILE_PATH)
    inserted_record=networkdata.pushing_data_to_mongodb(records,DATABASE_NAME,COLLECTION_NAME)
    print(inserted_record)
    
    