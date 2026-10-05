import asyncio

async def check_balance(account_id):
    reader, writer = await asyncio.open_connection("127.0.0.1", 4444)

    print(f"Requesting balance for {account_id}")

    writer.write(f"{account_id}\n".encode())
    await writer.drain()

    response = await reader.readline()

    writer.close()
    await writer.wait_closed()
    return f"Server response: {response.decode().strip()}"

async def main():
    print("Starting tasks with TaskGroup...")

    # Store results externally
    results = []

    async def run_and_store(account_id):
        result = await check_balance(account_id)
        results.append(result)

    async with asyncio.TaskGroup() as tg:
        tg.create_task(run_and_store("A100"))
        tg.create_task(run_and_store("B200"))
        tg.create_task(run_and_store("X999"))  # invalid

    # All tasks complete here
    print("\nResults:")
    for result in results:
        print(result)


asyncio.run(main())
