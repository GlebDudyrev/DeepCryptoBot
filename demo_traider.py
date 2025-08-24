import os
import ccxt

from connection_config import SPOT_CONFIG, LINEAR_CONFIG


class BybitDemoTraider():
    def __init__(self, type='spot'):
        self.type = type
        if type == 'spot':
            config = SPOT_CONFIG
        else:
            config = LINEAR_CONFIG

        self.exchange = ccxt.bybit(config)
        self.exchange.enable_demo_trading(True)
        self.markets = self.exchange.load_markets()

    def get_balance(self, code=None):
        default = {'debt': 0.0, 'free': 0.0, 'total': 0.0, 'used': 0.0}
        if code:
            balance = self.exchange.fetch_balance().get(code, default)
        else:
            balance = self.exchange.fetch_balance()
            
        return balance
    
    def get_prices(self, symbols=['BTC/USDT', 'ETH/USDT', 'SOL/USDT']):
        prices = {}
        
        for symbol in symbols:
            price = self.exchange.fetch_ticker(symbol=symbol)
            prices[symbol] = price['last']
        
        return prices            

    def create_order(self):
        pass

    def close_order(self):
        pass


if __name__ == '__main__':
    from pprint import pprint
    
    traider = BybitDemoTraider(type='linear')

    balance = traider.get_balance('COCO')
    pprint(balance)
    
    prices = traider.get_prices()
    pprint(prices)