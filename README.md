Brendan Toolan G00350190 - Emerging Technologies Project 2019 

Ubuntu commands for running web app
    export FLASK_APP=WebApp/webApp.py
    flask run

Project Layout 
    WebApp (folder)
        webApp.py - Flask Server
        templates (folder)
            homepage.html - homepage for app
        Model.ipynb - Jupyter notebook where model is made
        model.h5 - where model is saved from notebook then loaded into the flask
        theimage.png
        resizedImage.png

Research
    TensorFlow
        Tensorflow is an open source platform that is used for machine learning. The architecture of Tensor is three parts, 1). Preprocess data, 2). build model, 3). train the model. Tensorflow can be ran on many different platfroms such as Desktops(windows, linux, etc), cloud web services and mobile devices.
    
    Keras 
        Keras is a high level neural networks API thats written in Python. It can be ran on Tensorflow, Theano and CNTK. Keras API was "designed for human beings, not machines". Model is the core Keras data structure(two main types, Sequential model and Model class).

    Mnist dataset
        MNIST (Mixed National Institute of Standards and Technology) is a dataset of handwritten digits. The digits ranges fro 0 - 9 meaning 10 patterns. MNIST is extensively used for classification and image recognition tasks.


References
    https://www.tensorflow.org/
    https://www.guru99.com/what-is-tensorflow.html
    https://keras.io/
    https://www.infoworld.com/article/3336192/what-is-keras-the-deep-neural-network-api-explained.html
    http://yann.lecun.com/exdb/mnist/
    https://corochann.com/mnist-dataset-introduction-1138.html
