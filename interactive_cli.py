import questionary
from bot.orders import execute_trade
from bot.logging_config import setup_logging
import sys

def main():
    setup_logging()
    print("\n🚀 --- Binance Futures Interactive Bot ---\n")

    # 1. Select Symbol
    symbol = questionary.select(
        "Select Trading Pair:",
        choices=["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT"]
    ).ask()

    # 2. Select Side
    side = questionary.select(
        "Select Side:",
        choices=["BUY", "SELL"]
    ).ask()

    # 3. Select Order Type
    order_type = questionary.select(
        "Order Type:",
        choices=["MARKET", "LIMIT", "STOP_LIMIT"]
    ).ask()

    # 4. Input Quantity
    qty = questionary.text("Enter Quantity (e.g., 0.01):").ask()

    # 5. Conditional Inputs for Price
    price = None
    stop_price = None

    if order_type in ["LIMIT", "STOP_LIMIT"]:
        price = questionary.text(f"Enter {order_type} Price:").ask()

    if order_type == "STOP_LIMIT":
        stop_price = questionary.text("Enter Stop Price (Trigger):").ask()

    # Confirmation step (The 'Pro' touch)
    confirm = questionary.confirm(f"Confirm {side} {qty} {symbol} at {price or 'Market'}?").ask()

    if not confirm:
        print("❌ Order cancelled.")
        sys.exit()

    try:
        response = execute_trade(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=float(qty),
            price=float(price) if price else None,
            stop_price=float(stop_price) if stop_price else None
        )

        if response:
            print(f"\n✅ Success! Order ID: {response.get('orderId')}")
        else:
            print("\n❌ Order failed. Check trading.log.")

    except Exception as e:
        print(f"\n⚠️ Error: {e}")

if __name__ == "__main__":
    main()