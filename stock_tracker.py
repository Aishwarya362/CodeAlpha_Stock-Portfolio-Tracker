import csv

# 1. Hardcoded dictionary of stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOG": 140,
    "AMZN": 130
}


def display_available_stocks():
    print("Available stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print()


def get_valid_quantity(symbol):
    """Ask for a quantity and validate the input."""
    while True:
        try:
            qty = int(input(f"Quantity of {symbol} (or 0 to skip): "))
            if qty < 0:
                print("  Quantity cannot be negative. Try again.")
            else:
                return qty
        except ValueError:
            print("  Please enter a whole number. Try again.")


def main():
    print("=== Stock Portfolio Tracker ===\n")

    portfolio = {}          # symbol -> quantity
    total_investment = 0.0

    # 2. Let the user pick stocks from the available list
    print("Enter quantities for the stocks you own.")
    display_available_stocks()

    for symbol in STOCK_PRICES:
        qty = get_valid_quantity(symbol)
        if qty > 0:
            portfolio[symbol] = qty

    # 3. Calculate the total investment value
    if not portfolio:
        print("No stocks added. Total investment: $0")
        return

    print("\n--- Portfolio Summary ---")
    for symbol, qty in portfolio.items():
        value = STOCK_PRICES[symbol] * qty   # basic arithmetic
        total_investment += value
        print(f"{symbol}: {qty} x ${STOCK_PRICES[symbol]} = ${value:,.2f}")

    print("-" * 28)
    print(f"TOTAL INVESTMENT VALUE: ${total_investment:,.2f}")

    # 4. Optionally save the result to a file
    save = input("\nSave results to a file? (csv/txt/no): ").strip().lower()
    if save == "csv":
        with open("portfolio_summary.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Price", "Quantity", "Value"])
            for symbol, qty in portfolio.items():
                writer.writerow([symbol, STOCK_PRICES[symbol], qty, STOCK_PRICES[symbol] * qty])
            writer.writerow(["TOTAL", "", "", f"{total_investment:.2f}"])
        print("Saved to portfolio_summary.csv")
    elif save == "txt":
        with open("portfolio_summary.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("=======================\n")
            for symbol, qty in portfolio.items():
                f.write(f"{symbol}: {qty} x ${STOCK_PRICES[symbol]} = ${STOCK_PRICES[symbol] * qty:,.2f}\n")
            f.write(f"TOTAL INVESTMENT VALUE: ${total_investment:,.2f}\n")
        print("Saved to portfolio_summary.txt")
    else:
        print("Results not saved.")


if __name__ == "__main__":
    main()
