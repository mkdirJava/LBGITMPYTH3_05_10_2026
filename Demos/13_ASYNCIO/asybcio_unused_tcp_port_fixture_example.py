import asyncio
import pytest


#@pytest.mark.asyncio
async def test_unused_port_fixture(unused_tcp_port):
    """Test the unused TCP port fixture."""

    # Client connected callback "task" (it closes the streamwriter object)
    async def closer(_, writer):
        writer.close()

    # Start first sever on unused port
    server1 = await asyncio.start_server(closer, host='localhost',
                                         port=unused_tcp_port)
    # Try again (same port), it should raise an IOError
    with pytest.raises(IOError):
        await asyncio.start_server(closer, host='localhost', port=unused_tcp_port)

    server1.close()
    await server1.wait_closed()
