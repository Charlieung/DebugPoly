from flask import request, jsonify
from random import random
from flask import Flask
from flask_cors import CORS
from flask import g
from newspaper import Article

from sklearn.externals import joblib

app = Flask(__name__)
CORS(app)

text_clf = joblib.load('app/text_clf.pkl')

# @app.before_first_request
# def load_model():
#     text_clf = joblib.load('text_clf.pkl')


@app.route("/")
def hello():
    return "hello world"


def get_article(url):
    article = Article(url, language='en')
    article.download()
    article.parse()
    return article

    # return {
    #     "title": article.title,
    #     "text": article.text
    # }


@app.route("/v1/bias/")
def bias():
    #return str(random())
    url = request.args.get('url')
    article = get_article(url)
    # print(article_text)
    score = text_clf.predict_proba([article.text])
    response = {
        "score": str(score[0][0]),
        "title": article.title,
        "authors": article.authors,
        "date": article.publish_date.isoformat()[:10]
    }
    return jsonify(**response)

if __name__ == "__main__":
    app.run()
