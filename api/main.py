from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/prices")
@app.get("/")
def get_prices():
    response = str(requests.get(
        url="https://api-hykmtavaga-ez.a.run.app/prices",
        headers={"X-API-KEY": "#%@s@lvl9em}%30LcGSq@AETH"}
    ).json())
    return response


@app.get("/stocks")
def get_stocks():
    response = str(requests.get(
        url="https://api-hykmtavaga-ez.a.run.app/stocks",
        headers={"X-API-KEY": "#%@s@lvl9em}%30LcGSq@AETH"}
    ).json())
    return response

# todo:post endpoint for prices
