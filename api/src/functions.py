import os

audience = os.getenv("API_URL")
api_key = os.environ.get("API_KEY")

headers = {"X-API-KEY": api_key}
