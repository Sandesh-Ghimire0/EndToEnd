import os
import sys

import numpy as np 
import pandas as pd
import dill
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, X_test, y_train, y_test, models):
    try:
        report = {}

        
        for i in range(len(list(models))):

            model = list(models.values())[i]


            model.fit(X_train,y_train)
            if i==0:
                logging.info("Model training started")
        

            train_pred = model.predict(X_train)
            test_pred = model.predict(X_test)

            training_accuracy = r2_score(y_train, train_pred)
            test_accuracy = r2_score(y_test, test_pred)

            report[list(models.keys())[i]] = [training_accuracy,test_accuracy]

        
        return report


    except Exception as e:
        raise CustomException(e,sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)