from flask import request
from random import random
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "hello world"

@app.route("/v1/bias/")
def bias():
    return str(random(), request.data)

if __name__ == "__main__":
    app.run()
