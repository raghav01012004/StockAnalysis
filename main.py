import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

stock = ["AAPL" , "TSLA"]

stocks = yf.download(stock, start = "2010-01-01", end = "2022-12-31")

data = stocks.loc[:,'Close'].copy()

data.plot(figsize = (17, 8), fontsize = 18)
plt.style.use("seaborn")
plt.show()