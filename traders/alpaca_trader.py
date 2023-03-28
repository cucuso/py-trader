from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

PUBLIC_KEY = 'PKJ9OHYJCFGBKKZJ4GE0'
PRIVATE_KEY = '0AinBZzLOAmfOibc5XTffIz62tH64jylzOx6dGtZ'


def execute_trade(side, symbol):
    print(f'submitting trade order for [{side}] side and symbol [{symbol}]')
    trading_client = TradingClient(PUBLIC_KEY, PRIVATE_KEY, paper=True)

    market_order = trading_client.submit_order(
        MarketOrderRequest(
            # "BTC/USD"
            symbol=symbol,
            type='market',
            qty=1,
            side=OrderSide.BUY if side == 'buy' else OrderSide.SELL,
            time_in_force=TimeInForce.IOC
        )
    )
    print(f'executed order [{market_order}]')
