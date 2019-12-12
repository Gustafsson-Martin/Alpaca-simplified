import requests
import json
from api_keys import *

TRADE_URL = "https://paper-api.alpaca.markets"
DATA_URL = "https://data.alpaca.markets/v1"

headers = {
    "APCA-API-KEY-ID" : API_KEY_ID,
    "APCA-API-SECRET-KEY" : API_SECRET_KEY
}

body = {
    "symbol": "CIEN",
    "qty": 10,
    "side": "sell",
    "type": "market",
    "time_in_force": "day"
}

response = requests.post(BASE_URL + "/v2/orders", data=json.dumps(body),headers=headers)
#response = requests.get(BASE_URL + "/v2/account/configurations", data=json.dumps(body), headers=headers)
print(json.loads(response.content))
