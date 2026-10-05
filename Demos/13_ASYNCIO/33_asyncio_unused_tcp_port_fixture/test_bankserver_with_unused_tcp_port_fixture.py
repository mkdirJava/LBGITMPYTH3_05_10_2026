import asyncio, pytest
from bankserver import start_server

async def test_valid_account(unused_tcp_port):
    port = unused_tcp_port
    server = await start_server(port=port)
    async with server:
        # Start serving in background
        server_task = asyncio.create_task(server.serve_forever())
        try:
            reader, writer = await asyncio.open_connection("127.0.0.1", port)
            writer.write(b"A100\n")
            await writer.drain()
            response = await reader.readline()
            assert response.decode().strip() == "BALANCE:500"
            writer.close()
            await writer.wait_closed()
        finally:
            server_task.cancel()

async def test_invalid_account(unused_tcp_port):
    port = unused_tcp_port
    server = await start_server(port=port)
    async with server:
        server_task = asyncio.create_task(server.serve_forever())
        try:
            reader, writer = await asyncio.open_connection("127.0.0.1", port)
            writer.write(b"X999\n")
            await writer.drain()
            response = await reader.readline()
            assert response.decode().strip() == "ERROR: Account not found"
            writer.close()
            await writer.wait_closed()
        finally:
            server_task.cancel()