import asyncio

ACCOUNTS = {"A100": 500, "B200": 300, "C300": 900,}

async def handle_client(reader: asyncio.StreamReader,
                        writer: asyncio.StreamWriter):
    data = await reader.readline()
    account_id = data.decode().strip()

    print(f"Request for account: {account_id}")

    balance = ACCOUNTS.get(account_id)

    if balance is None:
        response = "ERROR: Account not found\n"
    else:
        response = f"BALANCE:{balance}\n"

    writer.write(response.encode())
    await writer.drain()

    writer.close()
    await writer.wait_closed()


# Make server configurable and return it
async def start_server(host="127.0.0.1", port=4444):
    server = await asyncio.start_server(handle_client, host, port)
    return server

# Only run when executed directly
if __name__ == "__main__":
    async def main():
        server = await start_server()
        print("Bank server running on port 4444...")

        async with server:
            await server.serve_forever()

    asyncio.run(main())