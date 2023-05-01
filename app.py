from flask import Flask, request, render_template
from flask_cors import CORS,cross_origin
import pandas as pd
import os
from data_loading.data_loader_prediction import pred_loader
from data_loading.data_loader import train_loader
from file_operation.filemethod import file_op
from data_prediction import prediction_model
from data_training import training_model


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predict():
    try:
       inputs= request.form
       print(inputs)
       l = []
       for i in inputs.values():
           l.append(i)
       print(l)
       load=train_loader()
       df=load.data_load()
       prediction_df = pd.DataFrame(l, index=df.drop(columns=['Price']).columns).T
       print(prediction_df)
       if not os.path.isdir('Output/'):
           os.makedirs('Output/',exist_ok=True)
       prediction_df.to_excel("Output/Output.xlsx",header=True,index=False)
       pred=prediction_model()

       prediction_data=pred.model_prediction()
       print(prediction_data)
       file=file_op()
       model_name=file.model_finder()
       model=file.model_loading(model_name=model_name)
       price=model.predict(prediction_data)

       return render_template('index.html', result_text="The Flight Price is {}".format(price[0]))

    except Exception as e:
        print("exception ocurred %s" %e)

@app.route("/predict", methods=['POST'])
@cross_origin()
def train():
    try:
        train=training_model()
        train.model_training()

        return render_template('index.html', result="Traininig of model is a success")

    except Exception as e:
        raise e


if __name__ == "__main__":
    app.run(host="0.0.0.0",port="6060")
