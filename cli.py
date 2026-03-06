import argparse
import json
import sys

from bot.orders import execute_trade
from bot.logging_config import setup_logging


def main():

    # Initialize professional logging
    logger = setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures CLI Trading Bot")

    # Define Mandatory Arguments
    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Direction: BUY or SELL")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT", "STOP_LIMIT"], help="Order type: MARKET or LIMIT")
    parser.add_argument("--qty", required=True, type=float, help="Quantity to trade")
    parser.add_argument("--stop_price", type=float, help="Stop Price (Required for STOP_LIMIT)")

    # Define Optional Argument for LIMIT orders
    parser.add_argument("--price", type=float, help="Price (Required for LIMIT orders)")

    args = parser.parse_args()

    try:

        logger.info(f"Initiating {args.type} {args.side} order for {args.symbol}")

        # Execute the trade
        response = execute_trade(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.qty,
            price=args.price,
            stop_price=args.stop_price
        )

        if response:

            # Format the output as requested by the assignment
            output = {
                "orderId": response.get("orderId"),
                "status": response.get("status"),
                "executedQty": response.get("executedQty"),
                "avgPrice": response.get("avgPrice", "N/A")
            }

            print("\n--- Order Success ---")
            print(json.dumps(output, indent=4))
            logger.info(f"Order Successful: {output['orderId']}")

        else:
            print("\n--- Order Failed ---")
            print("Check logs/trading.log for details.")

    except Exception as e:
        logger.error(f"CLI Error: {str(e)}")
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()