# -*- coding: utf-8 -*-

import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd
import numpy as np
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import random
from sklearn.preprocessing import Normalizer
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = "jahnvikhanna"

from flask_mysqldb import MySQL
mysql = MySQL(app)
#

#
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     input_text = db.Column(db.String(500), nullable=False)
#     prediction = db.Column(db.String(200), nullable=False)
#     def __repr__(self) -> str:
#         return f"{self.input_text} - {self.prediction}"


import joblib
pipe = "pipe.pkl"

# vectorizer = joblib.load(open(vector_save_name, 'rb'))
# message = "dear emad trust email find well receive attached form tcc refund deducted tax amount please fill send back u asap best regard mesfer smesfer srmanager text 171 f 96614168989 966558281100 e user domain com email file transmitted may confidential intended solely use addressed individual entityreceived email error kindly notify sender immediately disclose content person store copy information mediumsignatory tcc accepts liability damage caused virus transmitted emailtcc email file transmitted may confidential intended solely use addressed individual entityto person store copy information mediumemail view opinion presented email solely author necessarily represent tcc email file transmitted may confidential intended solely use addressed individual entityto person store copy information mediumemail view opinion presented email solely author necessarily represent tcc email file transmitted may confidential intended solely use addressed individual entityto person store copy information mediumemail view opinion presented email solely author necessarily represent tcc email file transmitted may confidential intended solely use addressed individual entityto person store copy information mediumemail view opinion presented email solely author necessarily represent tcc"

# vec = vectorizer.transform([message]).toarray()
# print(vec)
# print(len(vec.toarray()[0]))

# with open(model_save_name, 'rb') as f:
#     model_rnn = pickle.Unpickler(f)

# model_rnn = joblib.load(open(model_save_name, 'rb'))
pipe = joblib.load(open(pipe, 'rb'))

@app.route('/')
def home():
    # print(np.__version__)
    return render_template('index_saloni.html')
@app.route('/prediction.html')
def prediction():
    # print(np.__version__)
    return render_template('prediction.html')


@app.route('/contact.html')
def contact():
    # print(np.__version__)
    return render_template('contact.html')


@app.route('/about.html')
def about():
    # print(np.__version__)
    return render_template('about.html')


@app.route('/index_saloni.html')
def index_saloni():
    # print(np.__version__)
    return render_template('index_saloni.html')



@app.route('/instructions1.html')
def instructions1():
    # print(np.__version__)
    return render_template('instructions1.html')




@app.route('/instructions2.html')
def instructions2():
    # print(np.__version__)
    return render_template('instructions2.html')


@app.route('/predict_saloni.html')
def predict():
    # print(np.__version__)
    return render_template('predict_saloni.html')



# @app.route('/prediction_new.html')
# def prediction_new():
#     # print(np.__version__)
#     return render_template('prediction_new.html')



@app.route('/predictions.html')
def predictions():
    # print(np.__version__)
    return render_template('predictions.html')





@app.route('/predict',methods=['POST'])
def Output():
    columns=['OverallQual', 'YearBuilt', 'TotalBsmtSF', '1stFlrSF', 'GrLivArea',
       'FullBath', 'TotRmsAbvGrd', 'GarageCars', 'GarageArea', 'BsmtFinType1',
       'BsmtFinType2', 'MSZoning', 'Street']

    messages = []
    print("file name",request.form.get ('BSmntFinType1'))
    inp = []
    for m in  request.form.values():
        try:
            inp.append(int(m))
        except:
            # print(m)
            inp.append(m)

    # if l==messages:
    #         print("both are same or not ")
    # else:
    #     print(l)
    #     print(messages)


    # print(messages)
    # inp = [8, 2009, 600, 800, 2020, 2, 9, 2, 422, 'Unf', 'GLQ', 'RL', 'Grvl']
    print("Nauman1")
    inpt = pd.DataFrame([inp], columns=columns)
    output1 =pipe.predict(inpt)
    # print(f"price is {output1[0]}")
    # cursor = mysql.connection.cursor()
    # cursor.execute(
    #     "INSERT INTO `khanna_price`(`OverallQual`, `YearBuilt`, `TotalBsmtSF`, `1stFlrSF`, `GrLivArea`, `FullBath`, `TotRmsAbvGrd`, `GarageCars`, `GarageArea`, `BsmtFinType1`, `BsmtFinType2`, `MSZoning`, `Street`, `SalePrice`)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(8, 2009, 600, 800, 2020, 2, 9, 2, 422, 'Unf', 'GLQ', 'RL', 'Grvl',output1[0])
    #     )
    # print("Nauman2")
    #
    # mysql.connection.commit()
    #
    # # Closing the cursor
    # cursor.close()

    # vec = vectorizer.transform(messages).toarray()
    # output = ve1c
    # output = model_rnn.predict(vec)
    # print("simple", output)
    # print(output[0])
    # print(output[0][0])

    # data = [round(output[0][0], 2), round(output[0][1], 2)]

    # print(vec)
    # if output[0][0]:
    #     message = "Phishing"
    #
    # else:
    #     message = "Legit"

    # todo = Todo(input_text=messages, prediction=message)
    # db.session.add(todo)
    # db.session.commit()

    return render_template('index.html',items=f"Price of this house is  {round(np.exp(output1)[0],3)} $")

if __name__ == "__main__":
    # print("warnings version",warnings.__version__)
#     # print("Pickle Versio",pickle.format_version)
    app.run(host='0.0.0.0',port=8080)

    