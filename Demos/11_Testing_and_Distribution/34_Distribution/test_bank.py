import pytest
from bank import BankAccount, InsufficientFundsError

@pytest.mark.parametrize(
    "initial_balance, withdraw_amount, expected_balance",
    [
        (100.0, 20.0, 80.0),
        (50.0, 50.0, 0.0),
    ]
)
def test_withdraw_success(initial_balance, withdraw_amount, expected_balance):
    account = BankAccount(initial_balance)
    new_balance = account.withdraw(withdraw_amount)

    assert new_balance == expected_balance

@pytest.mark.parametrize(
    "initial_balance, withdraw_amount, expected_exception",
    [
        (100.0, 0.0, ValueError),
        (100.0, -10.0, ValueError),
        (100.0, 200.0, InsufficientFundsError),
    ],
    ids=["zero withdrawal", "negative withdrawal", "insufficient funds"]
)
def test_withdraw_failures(initial_balance, withdraw_amount, expected_exception):
    account = BankAccount(initial_balance)

    with pytest.raises(expected_exception):
        account.withdraw(withdraw_amount)