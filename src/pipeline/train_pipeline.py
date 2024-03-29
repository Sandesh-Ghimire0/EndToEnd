
import sys

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException



class TrainingPipeline:
    def __init__(self):
        pass

    def train(self):
        try:
            obj = DataIngestion()
            train_data,test_data=obj.initiate_data_ingestion()

            data_transformation=DataTransformation()
            train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

            modeltrainer=ModelTrainer()
            print(modeltrainer.initiate_model_trainer(train_arr,test_arr))

        except Exception as e:
            CustomException(e,sys)

    