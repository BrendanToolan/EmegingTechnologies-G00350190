# Adapted from https://www.palletsprojects.com/p/flask/
# Adapted from https://medium.com/analytics-vidhya/deploy-ml-models-using-flask-as-rest-api-and-access-via-flutter-app-7ce63d5c1f3b

from flask import Flask, render_template, request
import base64
import numpy as np
import keras as ks
#from keras.models import load_model
import flask as fl
from PIL import Image, ImageOps
import cv2
import tensorflow as tf


app = Flask(__name__)
model = ks.models.load_model('model.h5')

height = 28
width = 28
size = height, width

graph = tf.get_default_graph()

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/predict', methods=['POST'])
def predict():

    global graph
    with graph.as_default():
        encodedImg = fl.request.values[('imgBase64')]
        decodedImg = base64.b64decode(encodedImg[22:])

        with open('theimage.png', 'wb') as f:
            f.write(decodedImg)

        image = Image.open("theimage.png")

        resizedImg = ImageOps.fit(image, size, Image.ANTIALIAS)
        resizedImg.save("resizedImage.png")

        newImg = cv2.imread("resizedImage.png")

        grayScaleImage = cv2.cvtColor(newImg, cv2.COLOR_BGR2GRAY)

        grayScaleArray = np.array(grayScaleImage, dtype=np.float32).reshape(1, 784)
        grayScaleArray /= 255

        setPrediction = model.predict(grayScaleArray)
        getPrediction = np.array(setPrediction[0])

        predictNum = str(np.argmax(getPrediction))
        print(predictNum)

        return predictNum

   

if __name__ == "__main__":
    app.run