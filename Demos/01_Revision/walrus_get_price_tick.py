import random
from dataclasses import dataclass

@dataclass
class PriceTick:
    price: float
    prev_close: float


# Simulated market‑data feed
def get_price_update():
    """
    Simulates receiving a single price update from a market data source.
    Each call returns the next PriceTick, or None when the feed ends.
    """
    # Static simulated sequence (could be a stream, API, socket, etc.)
    if not hasattr(get_price_update, "data"):
        prev_close = 100.0
        prices = [100.1, 100.5, 101.8, 102.3, 102.0, 103.7, 104.2]
        # Convert to a list of PriceTick objects
        get_price_update.data = [
            PriceTick(price=p, prev_close=prev_close)
            for p in prices
        ]

    # Pop one update per call
    if get_price_update.data:
        return get_price_update.data.pop(0)

    return None  # No more data