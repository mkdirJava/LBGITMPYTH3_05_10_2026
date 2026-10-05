import asyncio, aiohttp

async def check_balance(session, account_id):
    url = "http://127.0.0.1:8080/balance"

    print(f"Requesting balance for {account_id}")

    async with session.post(url, json={"account_id": account_id}) as resp:
        data = await resp.json()

        return f"Server response: {data}"

async def main():
    print("Starting requests with TaskGroup...")

    results = []

    async def run_and_store(session, account_id):
        result = await check_balance(session, account_id)
        results.append(result)

    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(run_and_store(session, "A100"))
            tg.create_task(run_and_store(session, "B200"))
            tg.create_task(run_and_store(session, "X999"))  # invalid

    print("\nResults:")
    for result in results:
        print(result)

asyncio.run(main())