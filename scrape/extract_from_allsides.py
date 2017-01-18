from newspaper import Article
from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm

BIAS_DIV_ID = 'source-bias-info-block'

BIAS_NAME_TO_SCORE = {
    'Bias: Left': 0,
    'Bias: Lean Left': .25,
    'Bias: Center': .5,
    'Bias: Mixed': .5,
    'Bias: Lean Right': .75,
    'Bias: Right': 1
}


def url_to_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")


def extract_actual_article_url(article_soup):
    return article_soup.find_all('div', 'article-link-hidden')[0].get_text().strip()


# TODO: record how entry fails
def extract_article(url):
    try:
        soup = url_to_soup(url)
        bias_div = soup.find(id=BIAS_DIV_ID)
        bias_text = bias_div.img["title"]
        source = bias_div.a.get_text()
        article_url = extract_actual_article_url(soup)
        article = Article(article_url, language='en')
        article.download()
        article.parse()
        article.nlp()
        return {
            "title": article.title,
            "url": article_url,
            "text": article.text,
            "bias": bias_text,
            "source": source,
            "authors": article.authors,
            "keywords": article.keywords
        }

    except:
        return {}


def urls_to_df(urls):
    extracted = [extract_article(url) for url in tqdm(urls)]
    return pd.DataFrame(extracted, index=range(len(extracted)))
