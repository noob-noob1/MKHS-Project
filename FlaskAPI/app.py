import flask
from flask import Flask,jsonify,request, render_template
import json
from data_in import data_in
import numpy as np
import pickle


def load_models():
    file_name = "model.p"
    with open (file_name, "rb") as pickled:
        data = pickle.load(pickled)
        model= data["model"]
    return model

app=Flask(__name__)
@app.route('/predict', methods=['GET'])
def predict():
    # stub input features 
    request_json= request.get_json()        #so that you get answer in terminal
    x=request_json["input"]
    print(x) 
    x=np.array(data_in).reshape(1,-1)
    x_in= np.array(x).reshape(1,-1)
    #load_models
    model=load_models()
    prediction = model.predict(x)[0]        #selects the first value of the list, which is a one value list
    response= json.dumps({'response':prediction})
    return response, 200
    # return render_template("delete.html", variable= prediction)

if __name__=="__main__":
    app.run(debug=True)


