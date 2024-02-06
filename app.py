from flask import Flask,request,render_template

from src.pipeline.prediction_pipeline import InputData, PredictionPipeline
from src.pipeline.train_pipeline import TrainingPipeline


application = Flask(__name__)
app = application


def return_training_message():
    return render_template('training.html',data='Training started')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def prediction():
    if request.method == 'GET':
        return render_template('prediction_form.html')

    else:
        input_data = InputData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        


        pred_df=input_data.get_input_as_dataframe()
        # print(pred_df)

        predict_pipeline=PredictionPipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('prediction_form.html',results=results[0])
    

@app.route('/train',methods=['GET','POST'])
def train_model():
    if request.method == 'GET':
        return render_template('training.html',started="Training started")
    
    else:
        print("training stated")
        obj = TrainingPipeline()
        obj.train()
        return render_template('training.html',completed = "training completed")


if __name__=="__main__":      
    app.run(debug=True) 
