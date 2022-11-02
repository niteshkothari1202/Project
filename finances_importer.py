import json
import os
from pandas_datareader import data


# --------------------------- STOCKS & TIME ----------------------- #
# --------------------------- STOCKS WITH THEIR PRICE GROWTH ------------ #


def stock_price_downloading(start_time, end_time):
    f = open('risk_stock.json')
    bank_stocks = json.load(f)
    for stocks, symbol in bank_stocks.items():
        if os.path.isfile(f'stockprices\{stocks.replace(" ", "_")}.csv'):
            pass
        else:
            a = data.DataReader(symbol + '.NS', 'yahoo', start_time, end_time)
            a.to_csv(f'stockprices\{stocks.replace(" ", "_")}.csv')
# --------------------------- Transported to CSV ------------------------ #
