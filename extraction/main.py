import logging
import time
from datetime import datetime, timedelta
from typing import Optional
from google.cloud import storage
import os

from extraction.models import logger

DEST_BUCKET = os.environ.get('TARGET_GCS_BUCKET', 'gs://gonzalez-dynamic-pricing')
bucket_name = "gonzalez-dynamic-pricing/raw"


# todo: write blobs to GCS from FastAPI raw data
def write_to_blob(blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    with blob.open("w") as f:
        f.write(...)


TABLES = [
    "product",
    "productType",
    "batch",
]


def main():
    logging.basicConfig(level=logging.INFO)

    # do periodic extraction of the data from /raw
    while True:
        now = datetime.now()
        for table in TABLES:
            try:
                extract_raw_data(table, now)
            except Exception as e:
                ...
        sleep_time = 60 * 10
        logger.info("Next extraction scheduled at %s", datetime.now() + timedelta(seconds=sleep_time))
        time.sleep(sleep_time)


def extract_raw_data(table, now):
    """
1 get last extraction date (since)
2 to_parquet(table, since, now)
3 update peewee extraction date ?
    """


def to_parquet(table: str, since: Optional[datetime], until: datetime):
    data = ()
    data.to_parquet(f"{DEST_BUCKET}/{table}.parquet", partition_cols="ts")


if __name__ == "__main__":
    main()
