import json
import requests

class AlpacaApi():
    TRADE_URL = "https://paper-api.alpaca.markets/v2"
    DATA_URL = "https://data.alpaca.markets/v1"

    def __init__(self, API_KEY_ID, API_SECRET_KEY):
        self.headers = {"APCA-API-KEY-ID" : API_KEY_ID, "APCA-API-SECRET-KEY" : API_SECRET_KEY}

    def buy(self, symbol, quantity, **kwargs):
        data = self._data(symbol, quantity, "buy", **kwargs)
        return self._trade_request("/orders", data)

    def sell(self, symbol, quantity, **kwargs):
        data = self._data(symbol, quantity, "sell", **kwargs)
        return self._trade_request("/orders", data)

    def _post_request(self, url, data):
        response = requests.post(url, data = data, headers = self.headers)
        content = json.loads(response.content)
        if (response.status_code // 100 == 2):
            return True
        print("Error: " + content["message"])
        return False

    def _trade_request(self, route, data):
        return self._post_request(AlpacaApi.TRADE_URL + route, data)

    def _data_request(self, route, data):
        self._post_request(AlpacaApi.DATA_URL + route, data)

    def _data(self, symbol, quantity, side, **kwargs):
        data = {
            "symbol": symbol,
            "qty": quantity,
            "side": side,
            "type": kwargs.get("type", "market"),
            "time_in_force": kwargs.get("time_in_force", "day")
        }
        return json.dumps(data)
