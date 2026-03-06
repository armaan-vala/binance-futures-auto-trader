# Binance Futures CLI Trading Bot (USDT-M)

A professional-grade Python application designed to interact with the **Binance Futures Testnet**. This project demonstrates clean code architecture, robust error handling, and a focus on Developer Experience (DX) through an interactive CLI.

---

## 🎯 Project Objectives & Focus Areas

As per the assignment requirements, this project focuses on:

* **Separation of Concerns:** Distinct layers for API communication, business logic, and user interface.
* **Robustness:** Comprehensive validation and exception handling for network/API failures.
* **Observability:** Structured logging of the entire order lifecycle.
* **User Experience:** Clear output and an enhanced interactive mode.

---

## 📂 Project Structure

```text
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py           # Binance API wrapper (Client Layer)
│   ├── orders.py           # Trade execution logic (Command Layer)
│   ├── validators.py       # Input & parameter validation
│   └── logging_config.py   # Centralized logging setup
├── logs/
│   └── trading.log         # Persistent record of all operations
├── cli.py                  # Standard Argument-based CLI
├── interactive_cli.py      # BONUS: Enhanced Interactive UX
├── .env                    # Environment variables (API Keys)
└── requirements.txt        # Project dependencies


```

##  🛠️ Setup & Installation

1. Clone the Repository

```text
git clone <your-repo-link>
cd binance-futures-auto-trader
```

2. Environment Setup and env setup

Create a .env file in the root directory and add your Binance Testnet credentials:

```text
BINANCE_API_KEY=your_testnet_key
BINANCE_API_SECRET=your_testnet_secret
```

3. Install Dependencies

```text
pip install -r requirements.txt
```

## 🚀 How to Run

### Option 1: Standard CLI (Mandatory Requirement)

Run orders directly using flags : run the command in terminal
```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.01 --price 50000

```

### Option 2: Interactive Bot (Bonus Feature) 

Experience a menu-driven interface with dropdowns and confirmation prompts:
```
python interactive_cli.py
```

## ✨ Bonus Features Implemented

1. Extra Order Type (STOP-LIMIT)

```
Extended the backend to support STOP_LIMIT orders, handling the additional stopPrice parameter and mapping it correctly to the Binance STOP order type.
```

2. Enhanced CLI UX

```
Implemented a fully interactive menu using the questionary library, featuring:

Arrow-key navigation for symbols and sides.

Conditional inputs (only asks for price if the order type requires it).

Pre-execution confirmation prompt to prevent accidental trades.
```

## 📝 Logging & Validation

The bot maintains a strict logging policy in logs/trading.log. 
```
It captures:

Pre-flight Validation: Ensures symbols, sides, and quantities are valid before hitting the API.

Request Payloads: Logs the exact JSON sent to Binance.

API Responses: Logs successful Order IDs or detailed error messages (e.g., Notional Value errors).
```

## 🛠️ Assumptions
To ensure smooth execution, the following were assumed during development:

* Environment Configuration: It is assumed the user has a `.env` file correctly set up in the root directory containing valid `BINANCE_API_KEY` and `BINANCE_API_SECRET`.

* Minimum Notional Value: We assumed a minimum notional value of >$100 for `BTCUSDT` on the Binance Testnet. Orders falling below this threshold will be caught and logged as API errors (e.g., Error code -4164).

* Testnet Activation: The user has an active Binance Futures Testnet account and is using the provided base URL: `https://testnet.binancefuture.com`.

* Python Environment: The user is running Python 3.x with all dependencies from `requirements.txt` installed.