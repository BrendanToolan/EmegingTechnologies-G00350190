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

#@app.route('/predict', methods=['GET','POST'])
#def predict():
#    parseImg(request.get.data())

#    x = imread("theimage.png", mode='L')
 #   x = np.invert(x)
  #  x = imresize(x, (28,28))

#    x = x.reshape(1, 28, 28, 1)
#    with graph.as_default():
#        out = models.predict(x)
#        print(out)
#        print(np.argmax(out, axis=1))
#        response = np.array_str(np.argmax(out, axis=1))
#        return response
#        return {"message": theimage}
#
#    def parseImg(imgData):
#        imgstr = re.search(b'base64,(.*)', imgData).group(1)
#        with open('theimage.png', 'wb') as output:
#            output.write(base64.decodebytes(imgstr))