import asyncio

# coroutine definition
async def transfer_funds(from_account, to_account, amount):
    print(f"Starting transfer of £{amount}...")
    # simulate network/database delay
    await asyncio.sleep(2)
    print(f"Debiting £{amount} from {from_account}")
    await asyncio.sleep(1)
    print(f"Crediting £{amount} to {to_account}")
    return f"Transfer of £{amount} complete"

async def main():
    result = await transfer_funds("Alice", "Bob", 100)
    print(result)

asyncio.run(main())