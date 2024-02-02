import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
import numpy as np
import pandas as pd
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import evaluate_models, save_object


@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array, test_array):
        try:

            X_train,X_test,y_train,y_test = (
                train_array[:,:-1],
                test_array[:,:-1],

                train_array[:,-1],
                test_array[:,-1]
            )

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            model_report:dict = evaluate_models(X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test, models=models)

            df = pd.DataFrame.from_dict(data=model_report,orient='index').reset_index()
            df.rename(columns={'index':'models',0:'training_accuracy',1:'test_accuracy'},inplace=True)
            logging.info("Model report created")

            max_accuracy = df['test_accuracy'].values.max()
            index = np.where(df['test_accuracy'] == max_accuracy)[0][0]

            best_model = df.iloc[index]

            save_model = models[best_model.models]

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=save_model
            )

            return best_model


        except Exception as e:
            raise CustomException(e,sys)