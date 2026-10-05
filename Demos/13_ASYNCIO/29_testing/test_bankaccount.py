import pytest
from bankaccount import BankAccount, transfer

# Basic deposit test
async def test_deposit():
    acc = BankAccount("Alice", 100)
    await acc.deposit(50)
    assert acc.balance == 150

# Basic withdraw test
async def test_withdraw():
    acc = BankAccount("Alice", 100)
    await acc.withdraw(40)
    assert acc.balance == 60

# Insufficient funds
async def test_withdraw_insufficient_funds():
    acc = BankAccount("Alice", 50)
    with pytest.raises(ValueError):
        await acc.withdraw(100)
    # Balance should remain unchanged
    assert acc.balance == 50

# Successful transfer
async def test_successful_transfer():
    acc_a = BankAccount("Alice", 100)
    acc_b = BankAccount("Bob", 200)
    await transfer(acc_a, acc_b, 50)
    assert acc_a.balance == 50
    assert acc_b.balance == 250

# Failed transfer should not credit target account
async def test_failed_transfer_insufficient_funds():
    acc_a = BankAccount("Alice", 100)
    acc_b = BankAccount("Bob", 200)
    with pytest.raises(ValueError):
        await transfer(acc_a, acc_b, 150)
    # Ensure balances unchanged
    assert acc_a.balance == 100
    assert acc_b.balance == 200

# TaskGroup behaviour: one failure cancels others
async def test_taskgroup_transfer_failure():
    import asyncio

    acc_a = BankAccount("Alice", 100)
    acc_b = BankAccount("Bob", 200)
    acc_c = BankAccount("Charlie", 50)

    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(transfer(acc_a, acc_b, 50))   # should succeed
            tg.create_task(transfer(acc_b, acc_c, 100))  # may succeed
            tg.create_task(transfer(acc_c, acc_a, 200))  # will fail

    except* ValueError as eg:
        # Ensure at least one failure occurred
        assert any("Insufficient funds" in str(e) for e in eg.exceptions)

    # Ensure no invalid credit happened
    assert acc_c.balance <= 150  # safe upper bound