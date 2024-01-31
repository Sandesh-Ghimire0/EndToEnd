'''
The main purpose of data ingestion is that it fetch the data from souces like api, database and 
split it into train test and store it  into some folder
'''


import os
import sys

import pandas as pd
from src.components.data_transformation import DataTransformation
from src.exception import CustomException
from dataclasses import dataclass

from src.logger import logging
from sklearn.model_selection import train_test_split


'''
the dataclass decorator automatically generates the init() method and intializes the object and
assigns the provided values as attributes
for examples
class Person:
    name:str
    age:int

The object of Person class will be initailized as obj = Person(name='something',age=some_integer)
Now to access name we can write obj.name

DataIngestionConfig class provides us the path where the data should be stored
'''
@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path :str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','data.csv')



'''
DataIngestion class collects the data from the source and 
stores it in paths provided by DataIngestionConfig
'''

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    
    def initiate_data_ingestion(self):

        logging.info("Entered the data ingestion method")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Stored the dataset as DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)


            logging.info("Data ingestion completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e,sys)

        
if __name__=="__main__":
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)
        
