from bot.client import BinanceClient
from bot.validators import validate_trade_params

def execute_trade(symbol, side, order_type, quantity, price=None, stop_price=None):
    # Pass all 6 arguments to validator
    validate_trade_params(symbol, side, order_type, quantity, price, stop_price)
    
    api = BinanceClient()
    # Pass all 6 arguments to client
    response = api.place_futures_order(symbol, side, order_type, quantity, price, stop_price)
    
    return response