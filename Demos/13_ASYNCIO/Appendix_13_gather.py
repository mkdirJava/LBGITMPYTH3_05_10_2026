import asyncio

async def get_balance(name):
    await asyncio.sleep(1) # simulate network/database delay
    return f"{name}: £100"

async def main():
    results = await asyncio.gather(
        get_balance("Alice"),
        get_balance("Bob"),
        get_balance("Charlie"),
    )
    print(results)

asyncio.run(main())