import cufflinks
import matplotlib.pyplot as plt
from pandas import read_csv
from seaborn import histplot, heatmap
from plotly.offline import init_notebook_mode


init_notebook_mode(connected=True)
cufflinks.go_offline()


def analysis():
    # standard deviation
    # stock which can be classified as the most risky
    returns = read_csv('analysis.csv', index_col='Date')
    # riskiest over 20 years
    high_std = returns.std().idxmax()

    # Correlation
    fig, ax = plt.subplots(figsize=(5,5))
    heatmap(returns.corr(), annot=True,ax=ax)
    plt.savefig('pict\heatmap.png')



    # Ploting
    a = returns.plot(figsize=(9, 6))
    plt.legend()
    plt.savefig('pict\All_plot.png')

    # data visualisation
    y = returns.loc['2015-01-01':'2015-12-31']
    fig, ax = plt.subplots(figsize=(9, 6))
    histplot(y[high_std], kde=True, color="Green", bins=40,ax=ax,).set(title=f'{high_std} highest standard deviation')
    plt.savefig('pict\highest_STD.png')


    # Moving Averages
    x = 0
    for i in returns.keys():
        x += 1
        plt.figure(figsize=(9, 6))
        returns[i].loc['2020-1-1':'2021-1-1'].rolling(window=30).mean().plot(label="30 days moving average")
        returns[i].loc['2020-1-1':'2021-1-1'].rolling(window=15).mean().plot(label="15 days moving average")
        returns[i].loc['2020-1-1':'2021-1-1'].plot(label=f"{i} Closing Price")
        plt.legend()
        plt.savefig(f'pict\stock_{x}.png')


    time_window = 30
    diff = returns.diff(1).dropna()  # diff in one field(one day
    up_chg = 0 * diff
    down_chg = 0 * diff
    up_chg[diff > 0] = diff[diff > 0]
    down_chg[diff < 0] = diff[diff < 0]
    up_chg_avg = up_chg.ewm(com=time_window-1, min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window - 1, min_periods=time_window).mean()
    rs = abs(up_chg_avg / down_chg_avg)
    rsi = 100 - 100 / (1 + rs)

    y = 0
    for i in rsi.keys():
        y += 1
        plt.figure(figsize=(9,6))
        rsi[i].plot()
        plt.suptitle(f'RSI Index of {i}')
        plt.legend()
        plt.savefig(f'pict/rsi_{y}.png')
        plt.clf()

    # # return %  histogram
    returns_pct = returns.pct_change()
    for i in range(0, 5, 1):
        returns_pct[returns_pct.keys()[i]].hist(bins=100, label=returns_pct.keys()[i], alpha=0.5)
    plt.legend()
    plt.suptitle("Percentage Change of Stock")
    plt.savefig('pict\All_stock_hist.png')
