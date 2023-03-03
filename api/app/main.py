import json

from fastapi import FastAPI

from app.src.functions import get_garys_prices, make_garys_prices_speedy

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/prices")
def get_prices():
    prices = get_garys_prices()
    return make_garys_prices_speedy(prices)


@app.get("/demo_prices")
def get_demo_prices():
    with open("app/demo_data/prices_format_example.json") as f:
        prices = json.load(f)

    return prices
