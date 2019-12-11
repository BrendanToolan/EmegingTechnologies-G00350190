# Adapted from https://www.palletsprojects.com/p/flask/
# Adapted from https://medium.com/analytics-vidhya/deploy-ml-models-using-flask-as-rest-api-and-access-via-flutter-app-7ce63d5c1f3b

from flask import Flask, render_template, request
import base64
import numpy as np
from tensorflow.keras.models import load_model
import flask as fl
from PIL import Image, ImageOps
import cv2
import tensorflow as tf

app = Flask(__name__)
model = load_model('model.h5')

height=28
width=28
size = height, width

@app.route('/')
def home():
    return render_template('homepage.html')

#Code used to save the canvas a png image
#@app.route('/uploadimage', methods =['GET', 'POST'])
#def uploadimage():
#    theimage = (fl.request.values.get("theimage",""))
 #   print(theimage)
  #  decodedimg = base64.b64decode(theimage[22:])
   # with open("theimage.png", "wb") as f:
    #    f.write(decodedimg)
    
    #return {"message": theimage}

@app.route('/predict', methods=['POST'])
def predict():

    encodedImg = fl.request.values[('imgBase64')]
    decodedImg = base64.b64decode(encodedImg[22:])
    with open('theimage.png', 'wb') as f:
        f.write(decodedImg)

    #size=28,28
    image = Image.open("theimage.png")
    resizedImg = ImageOps.fit(image, size, Image.ANTIALIAS)
    resizedImg.save("resizedImage.png")
    resizedImg = cv2.imread('resizedImage.png')
    grayScaleImg = cv2.cvtColor(resizedImg, cv2.COLOR_BGR2GRAY)
    grayScaleArray = np.array(grayScaleImg, dtype=np.float32).reshape(1, 784)
    grayScaleArray /= 255

    setPredict = model.predict(grayScaleArray)
    getPredict = np.array(setPredict[0])

    predictedNum = str(np.argmax(getPredict))
    print(predictedNum)
    return predictedNum

  #  theimage = (fl.request.values.get("theimage",""))
  #  print(theimage)
  #  decodedimg = base64.b64decode(theimage[22:])
  #  with open("theimage.png", "wb") as f:
  #      f.write(decodedimg)
    
  #  return {"message": theimage}

  #  parseImg(request.get.data())

  #  x = imread("theimage.png", mode='L')
  #  x = np.invert(x)
  #  x = imresize(x, (28,28))

  #  x = x.reshape(1, 28, 28, 1)
  #  with graph.as_default():
  #      out = models.predict(x)
  #      print(out)
  #      print(np.argmax(out, axis=1))
  #      response = np.array_str(np.argmax(out, axis=1))
  #      return response
  #      return {"message": theimage}

  #  def parseImg(imgData):
  #      imgstr = re.search(b'base64,(.*)', imgData).group(1)
  #      with open('theimage.png', 'wb') as output:
  #          output.write(base64.decodebytes(imgstr))

if __name__ == "__main__":
    app.run