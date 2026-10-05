import asyncio
import aiofiles
import json

# Save account data asynchronously
async def save_accounts(accounts, filename):
    async with aiofiles.open(filename, "w") as f:
        data = json.dumps(accounts)
        await f.write(data)
    print("Accounts saved")

# Load account data asynchronously
async def load_accounts(filename):
    async with aiofiles.open(filename, "r") as f:
        data = await f.read()
        accounts = json.loads(data)
    print("Accounts loaded")
    return accounts

async def main():
    filename = "accounts.json"

    # Fake banking data
    accounts = {
        "A100": {"name": "Alice", "balance": 500},
        "B200": {"name": "Bob", "balance": 300},
    }

    # Write to file
    await save_accounts(accounts, filename)

    # Read from file
    loaded_accounts = await load_accounts(filename)

    print("\nAccount data:")
    for acc_id, details in loaded_accounts.items():
        print(f"{acc_id}: {details}")

asyncio.run(main())