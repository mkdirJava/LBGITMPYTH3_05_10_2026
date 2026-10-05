import asyncio
import random

async def fetch_balance(account_id):
    print(f"Fetching balance for {account_id}...")
    await asyncio.sleep(random.random())  # simulate network delay
    return {"account": account_id, "balance": 100}

async def main():
    account_ids = ["A100", "B200", "C300"]
    results = [None] * len(account_ids)

    async def run_and_store(index, account_id):
        results[index] = await fetch_balance(account_id)

    async with asyncio.TaskGroup() as tg:
        for i, acc in enumerate(account_ids):
            tg.create_task(run_and_store(i, acc))

    print("\nResults:")
    for result in results:
        print(result)

asyncio.run(main())
