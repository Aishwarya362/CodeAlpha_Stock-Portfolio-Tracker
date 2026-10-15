# Stock Portfolio Tracker 📈

A simple command-line portfolio tracker written in Python. Enter how many shares you own of each stock, and the app calculates your total investment value — with an option to save the summary as **CSV** or **TXT**.

> **Note:** Prices are hardcoded for demonstration purposes, not live market data.

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/stock-portfolio-tracker.git
   cd stock-portfolio-tracker
   ```
2. Run it (Python 3.7+, no external dependencies — uses only the standard library `csv`):
   ```bash
   python stock_portfolio.py
   ```

## How It Works

1. The app shows a fixed list of 5 stocks with hardcoded prices (AAPL, TSLA, MSFT, GOOG, AMZN).
2. You enter the quantity you own for each stock (enter `0` to skip one).
3. Input is validated — negatives and non-numbers are rejected and re-asked.
4. A portfolio summary is printed with per-stock value and a grand total.
5. Optionally save the summary:
   - `csv` → writes `portfolio_summary.csv` (opens nicely in Excel/Google Sheets)
   - `txt` → writes `portfolio_summary.txt`
   - `no` → just print to the screen

## Example Run

```
=== Stock Portfolio Tracker ===

Enter quantities for the stocks you own.
Available stocks and prices:
  AAPL: $180
  TSLA: $250
  MSFT: $320
  GOOG: $140
  AMZN: $130

Quantity of AAPL (or 0 to skip): 10
Quantity of TSLA (or 0 to skip): 0
Quantity of MSFT (or 0 to skip): 5
Quantity of GOOG (or 0 to skip): 0
Quantity of AMZN (or 0 to skip): 20

--- Portfolio Summary ---
AAPL: 10 x $180 = $1,800.00
MSFT: 5 x $320 = $1,600.00
AMZN: 20 x $130 = $2,600.00
----------------------------
TOTAL INVESTMENT VALUE: $6,000.00

Save results to a file? (csv/txt/no): csv
Saved to portfolio_summary.csv
```

## Project Structure

```
stock-portfolio-tracker/
├── stock_portfolio.py   # The tracker (single file)
└── README.md            # This file
```

## Ideas for Extension

- Pull **live prices** from an API (e.g., Yahoo Finance) instead of hardcoded values
- Add buy/sell transactions with a persistent portfolio file
- Plot portfolio allocation with matplotlib

## License

MIT — free to use and modify.
