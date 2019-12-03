from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('WebApp/static/homepage.html')


if __name__ == "__main__":
    app.run