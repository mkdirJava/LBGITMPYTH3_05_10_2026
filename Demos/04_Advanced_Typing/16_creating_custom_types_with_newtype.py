from typing import NewType

# --- Defining NewTypes ---
# Both are floats, but the type checker now treats them as unique
USD = NewType('USD', float)
EUR = NewType('EUR', float)
#USD = float
#EUR = float

def calculate_total_usd(balance: USD, deposit: USD) -> USD:
    return USD(balance + deposit)

# Valid usage
account_balance = USD(1000.00)
monthly_bonus = USD(500.0)
total = calculate_total_usd(account_balance, monthly_bonus)
print(f"Total in USD: {total}")

# POTENTIAL ERROR: This would pass with a Type Alias,
# but a static type checker (like MyPy) will flag this as an error:
travel_cash = EUR(450.0)
total_error = calculate_total_usd(account_balance, travel_cash)
#                                                  ^^^^^^^^^^^ should be a USD type!
print(f"Total in EUR: {total_error}")


