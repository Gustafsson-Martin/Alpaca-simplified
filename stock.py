from datetime import datetime

class Bar: # class name might need changing
    def __init__(self, data):
        self.time = data['t']
        self.high = data['h']
        self.low = data['l']
        self.close = data['c']
        self.open = data['o']
        self.volume = data['v']
        self.date = datetime.fromtimestamp(self.time).strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return f"{self.date} : {self.open}, volume = {self.volume}"

class Stock: # class name might need changing
    def __init__(self, name, data):
        self.name = name
        self.data = [Bar(bar) for bar in data]

    def __iter__(self):
        return iter(self.data)
