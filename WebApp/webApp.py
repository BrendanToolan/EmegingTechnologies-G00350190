# Adapted from https://www.palletsprojects.com/p/flask/
# Adapted from https://medium.com/analytics-vidhya/deploy-ml-models-using-flask-as-rest-api-and-access-via-flutter-app-7ce63d5c1f3b

from flask import Flask, render_template, request
import base64
import numpy as np
from tensorflow.keras.models import load_model
import flask as fl

app = Flask(__name__)
models = load_model('model.h5')


@app.route('/')
def home():
    return render_template('homepage.html')


if __name__ == "__main__":
    app.run

#Code used to save the canvas a png image
@app.route('/uploadimage', methods =['GET', 'POST'])
def uploadimage():
    theimage = (fl.request.values.get("theimage",""))
    print(theimage)
    decodedimg = base64.b64decode(theimage[22:])
    with open("theimage.png", "wb") as f:
        f.write(decodedimg)
    
    return {"message": theimage}