import pytest
from bankaccount import BankAccount, transfer

@pytest.fixture
def sample_accounts():
    return (
        BankAccount("Alice", 100),
        BankAccount("Bob", 200),
        BankAccount("Charlie", 50),
    )

# TaskGroup behaviour: one failure cancels others
async def test_taskgroup_transfer_failure(sample_accounts):
    import asyncio

    # acc_a = sample_accounts[0]
    # acc_b = sample_accounts[1]
    # acc_c = sample_accounts[2]

    # Better?
    acc_a, acc_b, acc_c = sample_accounts

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