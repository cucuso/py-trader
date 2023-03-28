import vectorbt as vbt

FAST_PERIOD = 10
SLOW_PERIOD = 20

# original was 10, 20
def get_signals(prices):
    #fast_ma = vbt.MA.run(prices, FAST_PERIOD, short_name='fast')
    #slow_ma = vbt.MA.run(prices, SLOW_PERIOD, short_name='slow')
    # entries = fast_ma.ma_crossed_above(slow_ma)
    # print(entries.loc[lambda x: x == True])
    # exits = fast_ma.ma_crossed_below(slow_ma)
    # print(exits.loc[lambda x: x == True])
    rsi = vbt.RSI.run(prices, window=21)
    entries = rsi.rsi_crossed_above(60)
    exits = rsi.rsi_crossed_below(30)

    return entries, exits
