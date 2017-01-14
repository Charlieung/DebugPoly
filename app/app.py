from random import random
from flask import Flask

app = Flask(__name__)

@app.route("/v1/bias/<url>")
def bias(url):
    return str(random())

if __name__ == "__main__":
    app.run()
