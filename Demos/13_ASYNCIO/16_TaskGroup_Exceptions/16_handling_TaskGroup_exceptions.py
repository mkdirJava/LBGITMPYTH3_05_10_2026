import asyncio
from bankaccount import BankAccount, transfer

async def main():
    acc_a = BankAccount("Alice", 100)
    acc_b = BankAccount("Bob", 200)
    acc_c = BankAccount("Charlie", 50)

    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(transfer(acc_a, acc_b, 50))  # may succeed or be cancelled!
            tg.create_task(transfer(acc_b, acc_c, 100)) # may succeed or be cancelled!
            tg.create_task(transfer(acc_c, acc_a, 200)) # will fail
            tg.create_task(transfer(acc_a, acc_b, 50))  # may succeed or be cancelled!

    except* ValueError as eg:
        print("\nOne or more transfers failed:")
        for exc in eg.exceptions:
            print(exc)

    print("\nFinal balances:")
    print(f"Alice: {acc_a.balance}")
    print(f"Bob: {acc_b.balance}")
    print(f"Charlie: {acc_c.balance}")

asyncio.run(main())