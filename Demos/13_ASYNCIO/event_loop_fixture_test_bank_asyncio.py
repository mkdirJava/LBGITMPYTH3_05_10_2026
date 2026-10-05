import pytest
from event_loop_fixture_banking_service import BankAccount, transfer

async def test_deposit():
    account = BankAccount(100)
    new_balance = await account.deposit(50)
    assert new_balance == 150


async def test_withdraw():
    account = BankAccount(100)
    new_balance = await account.withdraw(40)
    assert new_balance == 60


async def test_transfer():
    acc1 = BankAccount(200)
    acc2 = BankAccount(50)

    await transfer(acc1, acc2, 100)

    assert acc1.balance == 100
    assert acc2.balance == 150

async def test_insufficient_funds():
    account = BankAccount(50)

    with pytest.raises(ValueError):
        await account.withdraw(100)