from decimal import Decimal
from typing import TypeVar

Permitted = TypeVar("Permitted", int, float, Decimal, str)

def normalise_transaction_amount(amount: object) -> float:
    # Validate the incoming value dynamically by checking against the TypeVar's __constraints__ list.
    # Check the TypeVar constraints dynamically
    allowed_types = Permitted.__constraints__

    if isinstance(amount, allowed_types):
        if isinstance(amount, str):
            cleaned = amount.replace("£", "").replace(",", "")
            return float(cleaned)
        else:
            return float(amount)

    # If the type is NOT in the TypeVar's constraints, reject it
    raise TypeError(
        f"Unsupported type '{type(amount).__name__}'. "
        f"Allowed types: {[t.__name__ for t in allowed_types]}"
    )
transactions = [125, 89.30, Decimal("12.99"), "£1,045.90", {"value": "250.00", "currency": "GBP"}]
normalised = []

for t in transactions:
    try:
        normalised.append(normalise_transaction_amount(t))
    except TypeError as e:
        print(f"Skipping invalid transaction: {t} -> {e}")

print(normalised)