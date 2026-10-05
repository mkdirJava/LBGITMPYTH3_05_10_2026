# Generators are excellent for streaming data, backtesting,
# and building memory‑efficient ETL pipelines.
# The example below, Streams one tick at a time → not storing millions of prices in memory
# Ideal for backtesting, real‑time analytics, event-driven pipelines
def price_tick_stream(symbol):
    # Simulated price ticks for live data ingestion
    prices = [101.2, 101.4, 101.1, 101.9, 102.5]
    for p in prices:
        yield {"symbol": symbol, "price": p}


for tick in price_tick_stream("AAPL"):
    print("Received:", tick)

# More advanced Generator for risk simulation (Monte Carlo)
# Monte Carlo is widely used in:
# - option pricing
# - risk modelling (VaR, CVaR)
# - scenario generation
# - stress testing
# - simulating asset paths
# - pricing forwards/swaps under stochastic models
import random

def monte_carlo_paths(start, drift, vol, steps=5):
    price = start
    for _ in range(steps):
        price *= (1 + random.gauss(drift, vol))
        yield price

for p in monte_carlo_paths(100, 0.001, 0.02):
    print("Simulated path price:", p)


#Iterators in Financial Services
# An iterator is any object implementing:
# - __iter__()
# - __next__()
#
# They are perfect when you need custom sequential access.
# Example: Custom Iterator for Paginated Trade Records
# Risk and reporting systems often paginate trade queries from a DB or API.
# Why useful:
# - Large trade books often exceed RAM
# - Pulls just enough data to process a page
# - Used in regulatory ETL, market surveillance, clearing systems
class TradePageIterator:
    def __init__(self, fetch_page_fn, page_size=100):
        self.fetch_page = fetch_page_fn
        self.page_size = page_size
        self.page = []
        self.index = 0
        self.current_page_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.page):
            self.current_page_number += 1
            self.page = self.fetch_page(self.current_page_number, self.page_size)

            if not self.page:  # No more data
                raise StopIteration

            self.index = 0

        result = self.page[self.index]
        self.index += 1
        return result

def fake_fetch(page, size):
    # 3 pages of trades
    data = {
        1: [{"id": "T1"}, {"id": "T2"}],
        2: [{"id": "T3"}],
        3: []
    }
    return data.get(page, [])

for trade in TradePageIterator(fake_fetch):
    print("Processing trade:", trade)


# 3. Coroutines in Financial Services
# Coroutines (via async def) support concurrent I/O‑heavy workloads, such as:
# - Fetching market data from multiple sources
# - Running risk calculations concurrently
# - Ingesting streams into Kafka
# - Async API calls (e.g., OMS, EMS, pricing engines)
#
# Example: Async Market Data Aggregation (Coroutine)
# Why useful:
# - Fetch prices from multiple exchanges concurrently
# - Used for best execution, smart order routing, VWAP/TWAP algorithms
import asyncio
import random

async def get_price(symbol):
    await asyncio.sleep(random.uniform(0.1, 0.3))  # Simulate network delay
    return {"symbol": symbol, "price": random.uniform(100, 105)}

async def collect_prices(symbols):
    tasks = [asyncio.create_task(get_price(sym)) for sym in symbols]
    return await asyncio.gather(*tasks)

symbols = ["AAPL", "MSFT", "GOOG", "AMZN"]

# Advanced: Coroutine-based pipeline (Async ETL)
async def fetch_trades():
    for i in range(5):
        await asyncio.sleep(0.1)
        yield {"trade_id": f"T{i}", "amount": 1000 + i}

async def process_trades():
    async for trade in fetch_trades():
        trade["amount_gbp"] = trade["amount"] * 0.79
        print("Processed:", trade)

asyncio.run(process_trades())

prices = asyncio.run(collect_prices(symbols))
print(prices)

import os
import glob



def iter_paths(path, kind="files"):
    pattern = os.path.join(path, '*')

    def _iter_files():
        for item in glob.iglob(pattern):
            if os.path.isfile(item):
                yield item

    def _iter_dirs():
        for item in glob.iglob(pattern):
            if os.path.isdir(item):
                yield item

    if kind == "files":
        yield from _iter_files()
    elif kind == "dirs":
        yield from _iter_dirs()


for f in iter_paths("./", kind="files"):
    print("FILE:", f)

for d in iter_paths("./", kind="dirs"):
    print("DIR:", d)

print("*" * 50)
gen = iter_paths("./", kind="files")
# do-while style loop
fname = next(gen, False)      # run once before checking
while fname:
    print(fname)
    # get the next item at the *end* of the loop
    fname = next(gen, False)

folders = []
gen = iter_paths("./", kind="dirs")
folders.append(next(gen, False))
folders.append(next(gen, False))
folders.append(next(gen, False))

print("*" * 50)
# Generator expressions

principal = 1000
rate = 0.05
years = 10

# Generator expression: compute the value after each year
balances = (principal * (1 + rate) ** year for year in range(1, years + 1))

# Example uses
print("Yearly balances:")
for amount in balances:
    print(f"{amount:,.2f}", end="")


def echo():
    #received = None
    while True:
        received = yield
        print(received)
        if received == "quit":
            yield received
            break
        yield received

g = echo()
next(g)       # start it
print(g.send("hi"))  # sends "hi" into the generator
#next(g)
print(g.send("Boo"))
#next(g)
print(g.send("quit"))


def compound_interest(initial_balance, annual_rate):
    """Coroutine that tracks compound interest and accepts new deposits."""
    balance = initial_balance
    rate = annual_rate

    # Prime: initial yield returns the starting balance
    value = yield balance

    while True:
        if isinstance(value, dict):
            # Allow dynamic updates
            balance += value.get("deposit", 0)
            rate = value.get("rate", rate)

        # Apply one period of interest
        balance *= (1 + rate)

        # Yield updated balance and wait for next instruction
        value = yield balance

# Start with £1000, interest rate 5%
c = compound_interest(1000, 0.05)
print("Start:", next(c))

# Add £200 deposit
print("After deposit:", c.send({"deposit": 200}))

# Next period, no changes
print("Next period:", c.send({}))

# Change interest rate to 7%
print("After rate change:", c.send({"rate": 0.07}))

# Add £500 deposit
print("After another deposit:", c.send({"deposit": 500}))



