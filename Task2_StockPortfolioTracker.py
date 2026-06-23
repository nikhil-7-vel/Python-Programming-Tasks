# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "TCS": 3500,
    "INFY": 1600,
    "WIPRO": 450,
    "HCL": 1800,
    "RELIANCE": 2900
}

portfolio = {}
total_investment = 0

# Number of stocks to enter
n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock_name = input("\nEnter stock name (TCS, INFY, WIPRO, HCL, RELIANCE): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        portfolio[stock_name] = quantity
    else:
        print("Stock not found! Skipping...")

# Calculate total investment
print("\nPortfolio Summary")
print("-" * 30)

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}")

print("-" * 30)
print("Total Investment Value = $", total_investment)

# Save result to a text file
with open("portfolio_report.txt", "w") as file:
    file.write("Stock Portfolio Report\n")
    file.write("-" * 30 + "\n")

    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}\n")

    file.write("-" * 30 + "\n")
    file.write(f"Total Investment Value = ${total_investment}")

print("\nPortfolio report saved to 'portfolio_report.txt'")
