import asyncio
import random


async def fetch_balance(account_id):
    print(f"Fetching balance for {account_id}...")
    await asyncio.sleep(random.random())  # simulate network delay
    return {"account": account_id, "balance": 100}

async def main():
    # Create tasks (start immediately)
    task1 = asyncio.create_task(fetch_balance("A100"))
    task2 = asyncio.create_task(fetch_balance("B200"))
    task3 = asyncio.create_task(fetch_balance("C300"))

    print("Tasks created, doing other work...")

    # Await results later
    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(f"\nResults: {result1}, {result2}, {result3}")

asyncio.run(main())