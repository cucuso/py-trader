import requests, json
import time
import pandas as pd
import pandas_ta as pta
import vectorbt as vbt
import strategies.sma_strategy as sma

ticker = 'BTC-USD'
start = '2019-10-01 UTC'  # crypto is in UTC
end = '2021-03-01 UTC'
prices = vbt.YFData.download(ticker, start=start, end=end).get('Close')
# Create the Signals Portfolio
# key is stop loss!
pf = vbt.Portfolio.from_signals(prices, entries=sma.get_signals(prices)[0], exits=sma.get_signals(prices)[1], freq="D", init_cash=100_000, fees=0.0025, slippage=0.0025, sl_stop=0.025)
# Print Portfolio Stats and Return Stats
print(pf.stats())
print(pf.returns_stats())


