# In Python, you can add type hints to assignments using PEP 526 variable annotations.
# This means you can specify a type right when you assign a value, or even without assigning a value.

# Annotate a variable at assignment
price: float = 101.5
symbol: str = "AAPL"
quantity: int = 100
active: bool = True


# Annotate without assigning
rate: float       # No value yet
positions: dict   # Declared type only


# Annotating containers
from typing import List, Dict, Tuple

prices: List[float] = [101.2, 102.5, 103.8]
cats: List[str] = list()
sizes: Dict[str, int] = {"AAPL": 100, "MSFT": 50}
point: Tuple[int, int] = (10, 20)


# Or using modern built‑in generics (Python 3.9+):
prices: list[float] = [99.5, 101.1]
sizes: dict[str, int] = {"EURUSD": 1_000_000}


# Annotating multiple variables
# You can annotate the type once and assign multiple variables:
x: int
y: int
x, y = 10, 20

# or annotate and assign individually
a: float = 1.0
b: float = 2.5


# Explicit “Any” when type truly varies
from typing import Any
def get_value_from_somewhere(pos: int):
    mylist = ["Banana", 12, 34.5, True, ("a", 1)]
    return mylist[pos]

value: Any = get_value_from_somewhere(1)


# Annotating constants
PI: float = 3.14159
MAX_CONNECTIONS: int = 10


# Annotating instance attributes inside classes
class Trade:
    symbol: str
    price: float
    quantity: int

    def __init__(self, symbol: str, price: float, quantity: int):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity


# Example with financial logic
from typing import List

# Historical price series
prices: List[float] = [101.2, 102.5, 103.1, 104.0]

# Moving average window
window: int = 3

# Portfolio allocation weights
weights: list[float] = [0.4, 0.3, 0.3]

# FX rate (e.g., EUR/USD)
fx_rate: float = 1.085

# Position flag
is_open: bool = True



