from cffi_module import C
# ---- Python client (banking logic) ----

account = {
    "name": "Alice",
    "balance": 1000.0
}

def process_withdrawal(account, amount):
    result = C.withdraw(account["balance"], amount)

    if result < 0:
        raise ValueError("Insufficient funds")

    account["balance"] = result
    return result

# Unit tests
import pytest
def test_withdrawal():
    account["balance"] = 1000.00
    process_withdrawal(account, 200.0)
    assert account["balance"] == 800.00

def test_withdraw_too_much_raises_error():
    account["balance"] = 1000.00
    with pytest.raises(ValueError):
        process_withdrawal(account, 1000.01)
