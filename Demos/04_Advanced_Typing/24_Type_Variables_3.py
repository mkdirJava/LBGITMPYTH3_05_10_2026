from typing import Any

def normalise_transaction_amount(amount: Any) -> float:
    # Accepts amounts in various formats (string, int, float, dicts) and returns a clean float.
    if isinstance(amount, (int, float)):
        return float(amount)
    if isinstance(amount, str):
        cleaned = amount.replace("£", "").replace(",", "")
        return float(cleaned)
    if isinstance(amount, dict) and "value" in amount:
        return float(amount["value"])

    raise ValueError(f"Unsupported amount type: {type(amount)}")

transactions = [125, 89.30, "£1,045.90", {"value": "250.00", "currency": "GBP"}]

normalised = [normalise_transaction_amount(t) for t in transactions]

print(normalised) # [125.0, 89.3, 1045.9, 250.0]
