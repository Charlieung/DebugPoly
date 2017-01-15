import extract_article
import pandas as pd
from tqdm import tqdm
import sys

start_round = 0
if len(sys.argv) > 1:
    start_round = int(sys.argv[1])
    print(start_round)

urls = pd.read_csv('article_urls.csv', index_col="index", names=["index", "urls"])

STEP_SIZE = 100
n_rows = urls["urls"].shape[0]
for ii in tqdm(range(start_round*STEP_SIZE, n_rows, STEP_SIZE)):
    slice_end = min(ii+STEP_SIZE, n_rows)
    slice = urls["urls"].iloc[ii:slice_end]
    slice_frame = extract_article.urls_to_df(slice)
    filename = "dataset/article_data_slice" + str(ii) + "-" + str(slice_end) + ".csv"
    slice_frame.to_csv(filename)
    # print(ii, min(ii+STEP_SIZE, n_rows))
