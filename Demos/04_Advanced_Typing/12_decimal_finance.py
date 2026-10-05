# Python 3.10+ syntax
from decimal import Decimal

# A balance lookup may return a balance (Decimal) or None if not found
def get_balance(account_id: str) -> Decimal | None:
    # ... query store ...
    return Decimal("1250.75")  # or None

# Payment amounts may arrive in different forms (e.g., inbound API)
AccountId = str

def normalise_amount(amount: Decimal | int | str) -> Decimal:
    if isinstance(amount, Decimal):
        return amount
    if isinstance(amount, int):           # smallest unit (e.g., pence/cents)
        return Decimal(amount) / Decimal(100)
    # string from external system
    return Decimal(amount)

def process_payment(account_id: AccountId, amount: Decimal | int | str) -> bool:
    dec_amount = normalise_amount(amount)
    # ... perform checks, post ledger entry ...
    return True

amount: Decimal = Decimal("123.55")
print(process_payment("12345678", amount))

