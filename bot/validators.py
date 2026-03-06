import logging

logger = logging.getLogger("TradingBot.validators")

def validate_trade_params(symbol, side, order_type, quantity, price=None, stop_price=None):
    if side.upper() not in ['BUY', 'SELL']:
        raise ValueError("Side must be either 'BUY' or 'SELL'")

    allowed_types = ['MARKET', 'LIMIT', 'STOP_LIMIT']
    if order_type.upper() not in allowed_types:
        raise ValueError(f"Order type must be one of {allowed_types}")

    if order_type.upper() in ['LIMIT', 'STOP_LIMIT'] and price is None:
        raise ValueError(f"Price is mandatory for {order_type} orders")

    if order_type.upper() == 'STOP_LIMIT' and stop_price is None:
        raise ValueError("stop_price is mandatory for STOP_LIMIT orders")

    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than 0")

    logger.info(f"Validation successful for {symbol} {side}")
    return True