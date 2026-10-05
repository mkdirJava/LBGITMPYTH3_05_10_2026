import asyncio

ACCOUNTS = {
    "A100": 500,
    "B200": 300,
    "C300": 900,
}

async def handle_client(reader: asyncio.StreamReader,
                        writer: asyncio.StreamWriter):
    data = await reader.readline()
    account_id = data.decode().strip()

    print(f"Request for account: {account_id}")

    balance = ACCOUNTS.get(account_id, None)

    if balance is None:
        response = "ERROR: Account not found\n"
    else:
        response = f"BALANCE:{balance}\n"

    writer.write(response.encode())
    await writer.drain()

    writer.close()
    await writer.wait_closed()


async def start_server():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 4444)

    print("Bank server running on port 4444...")
    async with server:
        await server.serve_forever()


# Run server:
asyncio.run(start_server())