import datetime
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import time

dates = []
current_date = datetime.datetime.now()
dates.append(current_date.isoformat()[:10])

for ii in range(180):
    current_date = current_date - datetime.timedelta(days=4)
    dates.append(current_date.isoformat()[:10])


def get_urls_for_date(date):
    response = requests.get('http://www.allsides.com/?date_filter[value][date]=' + date)
    soup = BeautifulSoup(response.content, "html.parser")
    return [el.a.get('href') for el in soup.find_all('div', "news-title")]


all_urls = []

for date in tqdm(dates):
    all_urls.append(get_urls_for_date(date))
    time.sleep(10)


flattened_urls = [url for url_sublist in all_urls for url in url_sublist]
pd.Series(flattened_urls).to_csv('article_urls.csv')