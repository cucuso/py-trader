import vectorbt as vbt
import strategies.rsi_strategy as strategy
from datetime import datetime, timedelta
import time
import traders.alpaca_trader as trader

# set global variables
# interval is 1800 seconds which is 30 minutes.
interval = 60
ticker = 'BTC-USD'
last_action = 'sold'

print("Running pyTrader v0.0.1")


def print_signals(entries, exits):
    # prints all entries and exits..
    for entry, exit in zip(entries.items(), exits.items()):
        if entry[1]:
            print(f'{entry[0]} buy')
        if exit[1]:
            print(f'{exit[0]} sell')


def check_latest_signals():
    global last_action
    print(f'checking latest signals last action performed [{last_action}]')
    end = datetime.now()
    start = end - timedelta(hours=1)

    prices = vbt.YFData.download(ticker, start=start, end=end, interval="1m").get('Close')
    entries = strategy.get_signals(prices)[0]
    exits = strategy.get_signals(prices)[1]
    # check last signal every 30 minutes,if there is entry or exit, execute depending on last action performed
    if last_action == 'sold':
        last_entry_signal = entries.iloc[[-1]];
        print(f'last action was [{last_action}] checking latest entry signal [{last_entry_signal}]')
        if last_entry_signal[0]:
            print(f'latest exit signal is true, executing buy trade')
            trader.execute_trade('buy', 'BTC/USD')
            last_action = 'bought'
    elif last_action == 'bought':
        last_exit_signal = exits.iloc[[-1]];
        print(f'last action was [{last_action}] checking latest exit signal [{last_exit_signal}]')
        if last_exit_signal[0]:
            print(f'latest exit signal is true, executing sell trade')
            trader.execute_trade('sell', 'BTC/USD')
            last_action = 'sold'


while True:
    check_latest_signals()
    time.sleep(interval)
