import os
import sys
from typing import List, Tuple
import pandas as pd
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


class NetworkDataExtract():
    def __init__(self):
        try:
            #self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def read_csv_from_folder(self,file_path):
        
        """
        it read the data from the source
        """
        try:
            data=pd.read_csv(file_path)
            print(data)
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__=='__main__':
    DATA_FILE_PATH="./networkdata/network_data.csv"
    networkdata=NetworkDataExtract()
    networkdata.read_csv_from_folder(DATA_FILE_PATH)