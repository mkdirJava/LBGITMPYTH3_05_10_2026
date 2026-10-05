# Extract, Transform and Load(ETL)
# ETL is a type of pattern that is commonly used in
# front‑office, middle‑office, and regulatory‑reporting pipelines.
# Here's a finance‑oriented demo that uses a simple ETL pipeline in Python, using:
# - Dataclasses → to model structured financial records
# - Pandas DataFrames → for transformation and analytics
# - Functions to separate Extract, Transform, Load phases
# - Clean, idiomatic Python

# The below code creates a small ETL workflow that:
# - Extracts raw trade data (e.g., CSV, API, dicts)
# - Transforms it into strongly‑typed dataclass objects
# - Loads it into a pandas DataFrame
# - Performs typical finance transformations
#   - FX conversion
#   - Trade normalization
#   - Derived fields (e.g., notional value)

# STEP 1 — Model Structured Financial Data With Dataclasses
from dataclasses import dataclass
# dataclasses are a convenient way to create classes that primarily store
# data—without writing lots of boilerplate code. They were introduced in
# Python 3.7 to make simple data containers easier and cleaner to define.
# Python automatically creates the __init__ and __repr__ methods for you.
@dataclass
class TradeRecord:
    trade_id: str
    symbol: str
    quantity: int
    price: float
    currency: str

# STEP 2 - Extract Phase (E)
# Simulate ingestion from raw flat files or API responses:
import csv

def extract_trades(csv_path: str):
    """
    Extracts raw trade data from a CSV file.
    """
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

# STEP 3 - Transform Phase (T)
# Convert raw dicts → dataclass objects and apply financial transformations.
FX_RATES = {
    "USD": 0.79,   # into GBP
    "GBP": 1.00
}

def transform_trades(raw_records):
    """
    Converts raw CSV rows into structured TradeRecord objects
    and enriches data with derived fields.
    """
    trades = []

    for r in raw_records:
        trade = TradeRecord(
            trade_id=r["trade_id"],
            symbol=r["symbol"],
            quantity=int(r["quantity"]),
            price=float(r["price"]),
            currency=r["currency"],
        )

        trades.append(trade)

    return trades

# STEP 4 - Load Phase (L) into a DataFrame
import pandas as pd

def load_into_dataframe(trades):
    """
    Loads TradeRecord objects into a pandas DataFrame
    with derived financial metrics.
    """
    df = pd.DataFrame([t.__dict__ for t in trades])

    # Derived metrics
    df["notional"] = df["quantity"] * df["price"]
    df["notional_gbp"] = df["notional"] * df["currency"].map(FX_RATES)

    return df

# Putting It All Together
def run_etl(csv_path):
    raw = extract_trades(csv_path)
    structured = transform_trades(raw)
    df = load_into_dataframe(structured)
    return df


# Run pipeline
df = run_etl("raw_trade_data.csv")
print(df)

# Expected Output:
#   trade_id symbol  quantity   price currency  notional  notional_gbp
# 0       T1   AAPL       100  175.50      USD   17550.0       13864.50
# 1       T2  VOD.L      2000    0.98      GBP    1960.0        1960.00
# 2       T3   MSFT        50  311.20      USD   15560.0       12292.40