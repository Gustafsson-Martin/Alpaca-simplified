import requests
import json
from datetime import datetime
from api_keys import *
from stock import Stock

TRADE_URL = "https://paper-api.alpaca.markets/v2"
DATA_URL = "https://data.alpaca.markets/v1"

headers = {
    "APCA-API-KEY-ID" : API_KEY_ID,
    "APCA-API-SECRET-KEY" : API_SECRET_KEY
}

symbols = ['CIEN', 'TSLA', 'APPL']
symbols_string = ','.join(symbols)
print(symbols_string)


params = {
    "symbols": symbols_string,
    "limit": 1000
}

def buy(symbol, quantity, **kwargs):
    body = {
        "symbol": symbol,
        "qty": quantity,
        "side": "buy",
        "type": kwargs.get("type", "market"),
        "time_in_force": kwargs.get("time_in_force", "day")
    }
    response = requests.post(TRADE_URL + "/orders", data=json.dumps(body), headers=headers)
    content = json.loads(response.content)
    if (response.status_code // 100 == 2):
        print(("Bought %d stocks of %s") % (quantity, symbol))
    else:
        print("Error: " + content["message"])


def sell(symbol, quantity, **kwargs):
    body = {
        "symbol": symbol,
        "qty": quantity,
        "side": "sell",
        "type": kwargs.get("type", "market"),
        "time_in_force": kwargs.get("time_in_force", "day")
    }
    response = requests.post(TRADE_URL + "/orders", data=json.dumps(body), headers=headers)
    content = json.loads(response.content)
    if (response.status_code // 100 == 2):
        print(("Sold %d stocks of %s") % (quantity, symbol))
    else:
        print("Error: " + content["message"])

buy("CIEN", 10)
exit()
#response = requests.post(TRADE_URL + "/orders", data=json.dumps(body),headers=headers)
response = requests.get("https://data.alpaca.markets/v1/bars/1Min", params=params, headers=headers)
res = json.loads(response.content)
first_time = res['CIEN'][0]['t']
last_time = res['CIEN'][len(res['CIEN'])-1]['t']
first_datetime = datetime.fromtimestamp(first_time)
last_datetime = datetime.fromtimestamp(last_time)
print(first_datetime.strftime("%Y-%m-%d %H:%M:%S"))
print(last_datetime.strftime("%Y-%m-%d %H:%M:%S"))
print(res)
stocks = []
for r in res:
    stocks.append(Stock(r, res[r]))
    print(r)

print(stocks[1])

#for price in stocks[0]:
#    print(price.high)
#print(json.loads(response.content))
