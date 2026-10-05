from decimal import Decimal
from typing import TypeVar

Permitted = TypeVar("Permitted", int, float, Decimal, str)
def normalise_transaction_amount(amount: Permitted) -> float:
    if isinstance(amount, (int, float, Decimal)):
        return float(amount)

    if isinstance(amount, str):
        # Handle formatting like "£1,234.56" or "1,234.56"
        cleaned = amount.replace("£", "").replace(",", "")
        return float(cleaned)

transactions = [125, 89.30, Decimal("12.99"), "£1,045.90", {"value": "250.00", "currency": "GBP"}]

normalised = [normalise_transaction_amount(t) for t in transactions]

print(normalised)

# To demonstrate the issue rename the file to start with a non numeric and run mypy from terminal window

# ARE UNION and TYPEVAR the same?
# NO.
# Using union:
def first_1(a: int | str, b: int | str) -> int | str:
    return a
# The following calls are valid because each parameter independently allows either type.:
first_1(1, "x")
first_1("x", 1)
# Using TypeVar:
T = TypeVar("T", int, str)

def first_one(a: T, b: T) -> T:
    return a
# The follwing calls are valid
first_one(1, 2)      # OK
first_one("a", "b")  # OK
# But this one isn't because both arguments must be the same concrete type.
first_one(1, "a")    # Type checker error