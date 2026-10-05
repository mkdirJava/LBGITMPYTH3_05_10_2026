from dataclasses import dataclass

# Define incoming trade types
@dataclass
class MarketOrder:
    symbol: str
    quantity: int

@dataclass
class LimitOrder:
    symbol: str
    quantity: int
    limit_price: float

@dataclass
class FXSpotTrade:
    pair: str
    notional: float

@dataclass
class BondTrade:
    isin: str
    quantity: int
    price: float

# Process trades using match
def process_trade(trade):
    match trade:
        case MarketOrder(symbol=s, quantity=q):
            return f"Executing market order: BUY {q} {s}"

        case LimitOrder(symbol=s, quantity=q, limit_price=px):
            return f"Executing limit order: BUY {q} {s} at {px}"

        case FXSpotTrade(pair=p, notional=n):
            base, quote = p[:3], p[3:]   # Simple unpacking example
            return f"Booking FX spot trade: {n} {base}/{quote}"

        case BondTrade(isin=i, quantity=q, price=px):
            return f"Processing bond trade: {q} units of {i} at {px}"

        # Catch unknown types or malformed structures
        case _:
            return "Unrecognized trade type"


trades = [
    MarketOrder("AAPL", 100),
    LimitOrder("MSFT", 50, 310.25),
    FXSpotTrade("EURUSD", 5_000_000),
    BondTrade("US91282CAV37", 200, 98.45),
]

for t in trades:
    print(process_trade(t))