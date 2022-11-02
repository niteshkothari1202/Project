import json
import pandas
from analysis import *
# --------- STOCK IMPORTED FROM CSV ------------------ #
def prices():
    f = open('risk_stock.json')
    BANK_STOCKS = json.load(f)
    i = pandas.read_csv(f'stockprices\{list(BANK_STOCKS.items())[0][0].replace(" ", "_")}' + '.csv', index_col="Date")
    ii = pandas.read_csv(f'stockprices\{list(BANK_STOCKS.items())[1][0].replace(" ", "_")}.csv', index_col="Date")
    iii = pandas.read_csv(f'stockprices\{list(BANK_STOCKS.items())[2][0].replace(" ", "_")}.csv', index_col='Date')
    iv = pandas.read_csv(f'stockprices\{list(BANK_STOCKS.items())[3][0].replace(" ", "_")}.csv', index_col='Date')
    v = pandas.read_csv(f'stockprices\{list(BANK_STOCKS.items())[4][0].replace(" ", "_")}.csv', index_col='Date')
    # concatenating the data

    bank_stocks = pandas.concat([i, ii, iii, iv, v], axis=1, keys=BANK_STOCKS.keys())
    bank_stocks.columns.names = ['Bank Ticker', 'Stock Info']
    returns = pandas.DataFrame()
    for i in BANK_STOCKS.keys():
        returns[i] = bank_stocks[i]['Close']
    with open('analysis.csv', 'w') as fp:
        returns.to_csv(fp)
    analysis()


