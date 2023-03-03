import os

import requests

audience = os.getenv("API_URL")
api_key = os.environ.get("API_KEY")

headers = {"X-API-KEY": api_key}


def get_garys_prices():
    return requests.get(f"{audience}/prices", headers=headers).json()


def make_garys_prices_speedy(prices_json):
    return {
        category: {
            id: round(price_dict["gary"] * 0.9, 2)
            for id, price_dict in category_dict.items()
        }
        for category, category_dict in prices_json.items()
    }
