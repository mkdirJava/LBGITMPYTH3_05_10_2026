# Adding type hints to a function in Python is done using PEP 484 syntax.
# You annotate:
# - Parameters
# - Return type
# # This helps static type checkers (mypy, PyCharm), improves readability, and reduces bugs.

# Basic Function Type Hints
def add(x: int, y: int) -> int:
    return x + y

# x: int → parameter type
# y: int → parameter type
# -> int → return type


# Function With Multiple Parameter Types
def format_trade(symbol: str, price: float, quantity: int) -> str:
    return f"{quantity} of {symbol} at {price}"


# Optional Parameters
# Use Optional[...] or type | None (Python 3.10+):
from typing import Optional

def get_price(symbol: str, source: Optional[str] = None) -> float:
    if source is None:
        return 0.0
    return 10.0

#Modern Equivalent:
def get_price(symbol: str, source: str | None = None) -> float:
    if source is None:
        return 0.0
    return 10.0


# Functions Returning Multiple Values (tuples)
def fx_quote() -> tuple[float, float]:
    return 1.085, 1.087   # bid, ask


# Container Types
from typing import List, Dict

def moving_average(prices: List[float]) -> float:
    return sum(prices) / len(prices)

# Modern style:
def moving_average(prices: list[float]) -> float:
    return sum(prices) / len(prices)

# Functions Returning Nothing
def log_event(event: str) -> None:
    print(event)

# Callable Function Annotations
from typing import Callable

def apply_twice(fn: Callable[[float], float], x: float) -> float:
    return fn(fn(x))

#Financial Example — Pricer With Type Hints
def black_scholes_call(
    spot: float,
    strike: float,
    rate: float,
    vol: float,
    time: float
) -> float:
    pass

#Financial Example — FX Converter Function
def convert(amount: float, rate: float) -> float:
    return amount * rate

# Using Type Hints With Generators
import math
import random
from typing import Iterator


def monte_carlo_paths(
    start: float,
    drift: float,
    vol: float,
    steps: int = 252
) -> Iterator[float]:
    """
    Generate a Monte Carlo price path using a geometric Brownian motion (GBM)
    model.

    Parameters
    ----------
    start : float
        Initial asset price.
    drift : float
        Expected return (mu) per step.
    vol : float
        Volatility (sigma) per step.
    steps : int
        Number of time steps in the simulation (default = 252 trading days).

    Yields
    ------
    float
        The simulated price at each time step.
    """
    price = start

    for _ in range(steps):
        # Generate a random normally-distributed shock
        shock = random.gauss(0, 1)

        # GBM price update: S[t+1] = S[t] * exp( (mu - 0.5σ²) + σ * Z )
        price *= math.exp((drift - 0.5 * vol * vol) + vol * shock)

        yield price

# Basic example of calling monte-carlo-paths method
for p in monte_carlo_paths(100.0, drift=0.05/252, vol=0.2/math.sqrt(252), steps=5):
    print("Simulated price:", p)


# Collect the path into a list
path = list(monte_carlo_paths(
    start=100.0,
    drift=0.05/252,
    vol=0.2/math.sqrt(252),
    steps=10
))

print(path)


