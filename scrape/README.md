# Scape Allsides.com

This is a collection of command line utilities for scraping allsides.com for newspaper
articles annotated with crowdsourced bias information.

## To Scrape the dataset:

    python crawl_allsides_for_urls.py # stores a big list of urls in article_urls.csv
    python scrape_articles_from_urls.py # stores article text and meta data in aticles_with_bias_text.csv for each url in article_urls.csv

- `crawl_allsides_for_urls.py`
- `scrape_articles_from_urls.py`
- `extract_from_allsides_url.py``
