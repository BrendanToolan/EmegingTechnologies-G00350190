# Adapted from https://www.palletsprojects.com/p/flask/
# Adapted from https://medium.com/analytics-vidhya/deploy-ml-models-using-flask-as-rest-api-and-access-via-flutter-app-7ce63d5c1f3b
# Adapted from https://kobkrit.com/tensor-something-is-not-an-element-of-this-graph-error-in-keras-on-flask-web-server-4173a8fe15e1

#imports needed to run the python file
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
#loads the model
model = ks.models.load_model('model.h5')

#variables for the image and resized image
height = 28
width = 28
size = height, width

#added this into the code to avoid Tensor error, i.e. "Not an element of the graph"
graph = tf.get_default_graph()

#route to the html home page
@app.route('/')
def home():
    return render_template('homepage.html')

#POST method to get the predicted number, save the input on the canvas as a png and then resized that image
@app.route('/predict', methods=['POST'])
def predict():

    #added these two lines at 38 & 39 into the code to avoid Tensor error, i.e. "Not an element of the graph"
    global graph
    with graph.as_default():
        encodedImg = fl.request.values[('imgBase64')]
        #code that decodes the image
        decodedImg = base64.b64decode(encodedImg[22:])

        #creates input on canvas as 'theimage.png'
        with open('theimage.png', 'wb') as f:
            f.write(decodedImg)

        #opens and saves image
        image = Image.open("theimage.png")

        #code that takes the image, resizes it and then saves as new image 'resizedImage.png'
        resizedImg = ImageOps.fit(image, size, Image.ANTIALIAS)
        resizedImg.save("resizedImage.png")
        newImg = cv2.imread("resizedImage.png")
        
        grayScaleImage = cv2.cvtColor(newImg, cv2.COLOR_BGR2GRAY)

        grayScaleArray = np.array(grayScaleImage, dtype=np.float32).reshape(1, 784)
        grayScaleArray /= 255

        #set and get predictions that call from the model
        setPrediction = model.predict(grayScaleArray)
        getPrediction = np.array(setPrediction[0])

        #gets the predicted number from input on canvas
        predictNum = str(np.argmax(getPrediction))
        print(predictNum)

        #returns predicted digit that was inputed on canvas
        return predictNum

if __name__ == "__main__":
    app.run