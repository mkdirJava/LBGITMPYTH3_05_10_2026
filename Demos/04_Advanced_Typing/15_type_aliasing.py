import matplotlib.pyplot as plt
from typing import List, Tuple

# --- Type Aliasing ---
# Instead of List[Tuple[str, float]], we use meaningful names
Price = float
Timestamp = str
StockData = List[Tuple[Timestamp, Price]]

def plot_market_trend(data: StockData, ticker: str) -> None:
    # Uses StockData alias to handle historical pricing.
    # Unpack the list of tuples into separate lists for the x and y axes
    times, prices = zip(*data)

    plt.figure(figsize=(10, 5))
    plt.plot(times, prices, marker='o', linestyle='-', label='Price')

    # Standard Matplotlib formatting
    #plt.title(f"Intraday Performance: {ticker}", fontsize=14)
    #plt.xlabel("Trading Time (EST)")
    #plt.ylabel("Price (USD)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

# Sample dataset using our defined types
history: StockData = [("09:30", 182.50), ("10:30", 184.10), ("11:30", 183.75),
    ("12:30", 185.20), ("13:30", 187.05)]

plot_market_trend(history, "NVDA")
