from flask import Flask, render_template
import base64
import numpy as np
import keras as kr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')


if __name__ == "__main__":
    app.run


@app.route('/uploadimage', methods =['GET', 'POST'])
def uploadimage():
    theimage = (flask.request.get("theimage",""))
    print(theimage)
    decodedimg = base64.b64decode(theimage[22:])
    with open("theimage.png", "wb") as f:
        f.write(decodedimg)
    
    return {"message": theimage}