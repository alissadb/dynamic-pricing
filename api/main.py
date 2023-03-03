import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/prices")
def get_demo_prices():
    with open("demo_data/prices_format_example.json") as f:
        prices = json.load(f)

    return prices
