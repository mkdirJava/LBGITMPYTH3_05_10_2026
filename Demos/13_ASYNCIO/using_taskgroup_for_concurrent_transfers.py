from task_group_bank_account import BankAccount, transfer
import asyncio

async def main():
    acc_a = BankAccount("Alice", 500)
    acc_b = BankAccount("Bob", 300)
    acc_c = BankAccount("Charlie", 200)

    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(transfer(acc_a, acc_b, 100))
            tg.create_task(transfer(acc_b, acc_c, 50))
            tg.create_task(transfer(acc_c, acc_a, 75))

            # This one will fail (insufficient funds)
            tg.create_task(transfer(acc_c, acc_b, 500))

    except* ValueError as e:
        print("\n One or more transfers failed:")
        for err in e.exceptions:
            print(err)

    print("\nFinal balances:")
    print(f"Alice: {acc_a.balance}")
    print(f"Bob: {acc_b.balance}")
    print(f"Charlie: {acc_c.balance}")


asyncio.run(main())