import vectorbt as vbt

FAST_PERIOD = 10
SLOW_PERIOD = 20

# original was 10, 20
def get_signals(prices):
    fast_ma = vbt.MA.run(prices, FAST_PERIOD, short_name='fast')
    slow_ma = vbt.MA.run(prices, SLOW_PERIOD, short_name='slow')

    print(fast_ma.ma)
    print(slow_ma.ma)

    entries = fast_ma.ma_crossed_above(slow_ma)
    print('entries')
    print(entries.loc[lambda x: x == True])
    exits = fast_ma.ma_crossed_below(slow_ma)
    print('exits')
    print(exits.loc[lambda x: x == True])
    return entries, exits
