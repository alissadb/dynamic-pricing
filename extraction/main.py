import json
import logging
import time
from datetime import datetime, timedelta
from google.cloud import storage
import pandas as pd

from api.main import get_prices, get_stocks

client = storage.Client(project='speedy-gonzalez-379510')
bucket = client.get_bucket('gonzalez-dynamic-pricing')
TEAM_NUMBER = "3"


# read json from API and upload raw data to bucket
def upload_json_to_bucket(data, blob_name):
    blob = bucket.blob(blob_name)

    blob.upload_from_string(
        data=data,
        content_type='application/json'
    )


def download_json_from_bucket(blob_name):
    blob = bucket.blob(blob_name)

    return json.loads(blob.download_as_string(client=None))


def main():
    # extract_raw_data() // todo: fix
    products = download_json_from_bucket('raw/prices.json')
    stocks = download_json_from_bucket('raw/stocks.json')

    products_df = pd.DataFrame([
        {
            "id": str(product["id"]),
            "sell_by": product["sell_by"],
            "name": product_name,
            "category": category_name,
        }
        for category_name, category in products.items()
        for product_name, product in category["products"].items()
    ])

    stocks_df = pd.DataFrame([
        {"product_id": str(product_id), "quantity": quantity}
        for product_id, quantity in stocks[TEAM_NUMBER].items()
    ])

    df_merged = pd.merge(products_df, stocks_df, left_on="id", right_on="product_id", how="left")

    df = (
        df_merged.assign(
            timestamp=pd.to_datetime(df_merged['ts_ms'] / 1000, unit='s', origin='unix').dt.strftime('%Y-%m-%dT%H')
        )
    )

    df.to_parquet(f"gs://{bucket}/warehouse/test.pq", engine="pyarrow")


def extract_raw_data():
    # do periodic extraction of the data from /raw
    sleep_time = 60 * 10
    while True:
        now = datetime.now()
        try:
            upload_json_to_bucket(get_prices(), 'raw/prices.json')
            upload_json_to_bucket(get_stocks(), 'raw/stocks.json')

            # logger.info("Next extraction scheduled at %s", datetime.now() + timedelta(seconds=sleep_time))
            time.sleep(sleep_time)
        except Exception as e:
            logging.error("error")


# read from bucket as batches
# convert to parquet (pyarrow/spark/pandas)
# upload to bucket (silver)


if __name__ == "__main__":
    main()
