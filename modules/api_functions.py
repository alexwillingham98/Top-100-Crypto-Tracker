import requests
import json


with open(f"config/secrets.json") as f:
    secrets = json.load(f)

token = secrets["token"]

def get_price(id):

    

    url = "https://api.coingecko.com/api/v3/simple/price"

    headers = {
        "accept": "application/json",
        "token": token
    }

    data = {
        "vs_currencies" : "usd",
        "ids": id
    }

    response = requests.get(url, headers=headers, params=data)
    print(response.text)

def get_top_100_coins():

    url = "https://api.coingecko.com/api/v3/coins/markets"

    headers = {
    "accept": "application/json",
    "token": token
    }

    data = {
        "vs_currency" : "usd"
    }

    response = requests.get(url, headers=headers, params=data)
    return response.json()


