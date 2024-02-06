import sys
import os

import pandas as pd

from src.exception import CustomException
from src.utils import load_object

class TrainingException(Exception):
    def __init__(self,error_message):
        super().__init__(error_message)
        self.error_message="Trianing not initiated. Goto /train at first"
    
    def __str__(self):
        return self.error_message


class PredictionPipeline:
    def __init__(self):
        pass


    def predict(self,input):
        try:
            model_path = os.path.join('artifacts','model.pkl')
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)

            preprocessed_data = preprocessor.transform(input)
            pred = model.predict(preprocessed_data)

            return pred
        
        except Exception as e:
            raise TrainingException(e)



class InputData:
    def __init__(
            self,
            gender: str,
            race_ethnicity: str,
            parental_level_of_education:str,
            lunch: str,
            test_preparation_course: str,
            reading_score: int,
            writing_score: int

    ):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_input_as_dataframe(self):
        try:
            input_data_dict = {
                "gender":[self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(input_data_dict)

        except Exception as e:
            raise CustomException(e,sys)