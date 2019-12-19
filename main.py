import requests
import json
from datetime import datetime
from api_keys import *

TRADE_URL = "https://paper-api.alpaca.markets/v2"
DATA_URL = "https://data.alpaca.markets/v1"

headers = {
    "APCA-API-KEY-ID" : API_KEY_ID,
    "APCA-API-SECRET-KEY" : API_SECRET_KEY
}

symbols = ["CIEN", "WPX", "TSLA"]
symbols_string = ""
for symbol in symbols:
    symbols_string += symbol + ","
symbols_string = symbols_string[:-1]

print(symbols_string)

#body = {
#    "symbol": "CIEN",
#    "qty": 60,
#    "side": "buy",
#    "type": "market",
#    "time_in_force": "day"
#}

params = {
    "symbols": symbols_string,
    "limit": 1000
}


#response = requests.post(TRADE_URL + "/orders", data=json.dumps(body),headers=headers)
response = requests.get("https://data.alpaca.markets/v1/bars/1Min", params=params, headers=headers)
res = json.loads(response.content)
first_time = res['CIEN'][0]['t']
last_time = res['CIEN'][len(res['CIEN'])-1]['t']
first_datetime = datetime.fromtimestamp(first_time)
last_datetime = datetime.fromtimestamp(last_time)
print(first_datetime.strftime("%Y-%m-%d %H:%M:%M"))
print(last_datetime.strftime("%Y-%m-%d %H:%M:%M"))

for r in res:
    print(r)
#print(json.loads(response.content))
