# itemgetter is especially useful in FS data pipelines because it is:
# - Faster than lambdas
# - Cleaner for field extraction
# - Ideal when working with lists of dicts, tuples, and rows
# #
# Scenario: Sorting Trade Records by Price and Quantity
# Imagine you have a list of executed trades coming from an execution management system (EMS).
# You want to sort or extract columns efficiently.
from operator import itemgetter

# Example 1: Sorting Trades by Price Using itemgetter
# Trade feed (typical structure):
trades = [
    {"trade_id": "T1", "symbol": "AAPL", "qty": 100, "price": 175.50},
    {"trade_id": "T2", "symbol": "MSFT", "qty": 50,  "price": 311.20},
    {"trade_id": "T3", "symbol": "AAPL", "qty": 200, "price": 174.80},
    {"trade_id": "T4", "symbol": "GOOG", "qty": 5,   "price": 2795.00},
]

sorted_by_price = sorted(trades, key=itemgetter("price"))
print(sorted_by_price)

# Example 2: Multi‑Key Sorting (Symbol then Price)
# Useful for order books, TCA, risk factor grouping, etc.
sorted_by_sym_price = sorted(trades, key=itemgetter("symbol", "price"))
print(sorted_by_sym_price)

# Example 3: Extracting Columns Efficiently (symbol, qty)
# This mirrors ETL transformations when building fact tables for risk or P&L.
extract_symbol_qty = itemgetter("symbol", "qty")

for t in trades:
    print(extract_symbol_qty(t))
    # output:
    # ('AAPL', 100)
    # ('MSFT', 50)
    # ('AAPL', 200)
    # ('GOOG', 5)

# Example 4: Selecting Best Execution Based on Price
# Suppose you receive quotes from multiple liquidity providers (LPs) and want the best price.
quotes = [
    ("LP1", 1.1250),
    ("LP2", 1.1248),
    ("LP3", 1.1253),
]
# Best price = lowest.
# itemgetter(1) extracts the price field from each tuple.
best = min(quotes, key=itemgetter(1))
print(best) # output: ('LP2', 1.1248)
