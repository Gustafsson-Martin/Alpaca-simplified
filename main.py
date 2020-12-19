import requests
import json
from datetime import datetime
from api_keys import API_KEY_ID, API_SECRET_KEY
from stock import Stock
from alpacaApi import AlpacaApi


api = AlpacaApi(API_KEY_ID, API_SECRET_KEY)
#api.sell("TSLA", 1)
#exit()

symbols = ['CIEN', 'TSLA', 'APPL']
symbols = ['TSLA']
symbols_string = ','.join(symbols)
print(symbols_string)




time = "2020-12-17 00:00:00"
datetime_obj = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
print(datetime_obj.timestamp())

params = {
    "symbols": symbols_string,
    "limit": 5,
    "start": "2019-04-15T09:30:00-04:00",
}

response = requests.get("https://data.alpaca.markets/v1/bars/1Min", params=params, headers=api.headers)
res = json.loads(response.content)
first_time = res['TSLA'][0]['t']
last_time = res['TSLA'][len(res['TSLA'])-1]['t']
first_datetime = datetime.fromtimestamp(first_time)
last_datetime = datetime.fromtimestamp(last_time)
print(first_datetime.strftime("%Y-%m-%d %H:%M:%S"))
print(last_datetime.strftime("%Y-%m-%d %H:%M:%S"))
print(res)
stocks = []
for r in res:
    stocks.append(Stock(r, res[r]))
    print(r)

for bar in stocks[0]:
    print(bar)

#for price in stocks[0]:
#    print(price.high)
#print(json.loads(response.content))
