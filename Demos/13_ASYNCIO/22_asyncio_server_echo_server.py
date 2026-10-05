import asyncio

#connection socket
my_socket = '127.0.0.1', 4444

#reader is StreamReader
#writer is StreamWriter
async def my_server(reader, writer):
    #loop forever
    while True:
        #read upto 128 bytes
        #received_data = await reader.read(128)
        received_data = await reader.readline()
        if not received_data:
            break
        #write data to socket immediately (or queue to write buffer)
        writer.write(received_data.upper())
        ...
        #flow control; block until size of write buffer is low
        #(client has consumed)
        await writer.drain()
    #close the stream and the underlying socket
    writer.close()

async def main(host, port):
    #my_server is connected client callback coroutine
    server = await asyncio.start_server(my_server, host, port)
    ...
    #handle request until specific shutdown request
    await server.serve_forever()

#high-level execution of the coroutine
asyncio.run(main(*my_socket))
