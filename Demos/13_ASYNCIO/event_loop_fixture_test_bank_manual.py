import asyncio
from event_loop_fixture_banking_service import BankAccount, transfer

def test_deposit_manual():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    account = BankAccount(100)
    result = loop.run_until_complete(account.deposit(50))

    assert result == 150

    loop.close()


def test_transfer_manual():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    acc1 = BankAccount(200)
    acc2 = BankAccount(50)

    loop.run_until_complete(transfer(acc1, acc2, 100))

    assert acc1.balance == 100
    assert acc2.balance == 150

    loop.close()