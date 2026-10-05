import asyncio
import random

async def fetch_balance(account_id):
    print(f"Fetching balance for {account_id}...")
    await asyncio.sleep(random.random())  # simulate network delay
    return {"account": account_id, "balance": 100}

async def main():
    print("Starting tasks with TaskGroup...")

    # Store results externally
    results = []

    async def run_and_store(account_id):
        result = await fetch_balance(account_id)
        results.append(result)

    async with asyncio.TaskGroup() as tg:
        tg.create_task(run_and_store("A100"))
        tg.create_task(run_and_store("B200"))
        tg.create_task(run_and_store("C300"))

    # All tasks complete here
    print("\nResults:")
    for result in results:
        print(result)

asyncio.run(main())
