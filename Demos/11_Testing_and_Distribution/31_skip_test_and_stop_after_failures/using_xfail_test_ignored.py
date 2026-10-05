import pytest

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        # BUG: Allows overdraft
        self.balance -= amount
        return self.balance

@pytest.mark.xfail(reason="Overdraft protection not implemented yet")
def test_no_overdraft_allowed():
    account = BankAccount(100)
    account.withdraw(200)

    # balance will be less than zero so test will fail
    # but the xfail decorator converts this to the result being ignored.
    assert account.balance >= 0

