import os
import logging
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("TradingBot.client")

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        self.client = Client(self.api_key, self.api_secret, testnet=True)
        logger.info("Connected to Binance Futures Demo/Testnet.")

    def place_futures_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            params = {
                'symbol': symbol.upper(),
                'side': side.upper(),
                'quantity': quantity,
            }
            
            ot_upper = order_type.upper()
            if ot_upper == 'MARKET':
                params['type'] = 'MARKET'
            elif ot_upper == 'LIMIT':
                params['type'] = 'LIMIT'
                params['price'] = price
                params['timeInForce'] = 'GTC'
            elif ot_upper == 'STOP_LIMIT':
                params['type'] = 'STOP'  
                params['price'] = price
                params['stopPrice'] = stop_price
                params['timeInForce'] = 'GTC'

            logger.info(f"Sending Order Request: {params}")
            response = self.client.futures_create_order(**params)
            return response
        except Exception as e:
            logger.error(f"Order Placement Failed: {str(e)}")
            return None