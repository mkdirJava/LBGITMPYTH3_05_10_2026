import asyncio
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from pydantic import BaseModel

class ServerRequest(BaseModel):
    customer_id: int
    name: str

class ServerResponse(BaseModel):
    is_successful: bool


def run_server():
    print("[Server] Starting blocking listener...")
    my_socket = socket(AF_INET, SOCK_STREAM, 0)
    my_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    
    my_socket.bind(('127.0.0.1', 9000))
    my_socket.listen(1)

    new_socket, received_address = my_socket.accept()
    with new_socket:
        data_string = new_socket.recv(4096, 0).decode('utf-8')
        server_request = ServerRequest.model_validate_json(data_string)
        print(f"[Server] Received data: {server_request}")
        new_socket.sendall(ServerResponse(is_successful=True).model_dump_json().encode('utf-8'))
        print(f"[Server] Senht Data")
    my_socket.close()

def run_sender():
    print("[Sender] Attempting connection...")
    with  socket(AF_INET, SOCK_STREAM, 0) as my_socket_sender:
        my_socket_sender.connect(('127.0.0.1', 9000))
        data_payload = ServerRequest(customer_id=999,name="home").model_dump_json()
        data_payload_bytes= data_payload.encode('utf-8')
        print("[Sender] Attempting to send data...")
        my_socket_sender.sendall(data_payload_bytes)
        print("[Sender] Attempting To Reciveve data...") 
        data_string = my_socket_sender.recv(4096, 0).decode('utf-8')
        server_response = ServerResponse.model_validate_json(data_string)
        print(f"[Sender] RECCIEVED data {server_response}") 
        
    print("[Sender] Message sent and closed.")


import asyncio
from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
import random 
import time
import os

def run_udp_server():
    print("[UDP Server] Starting blocking listener...")
    my_socket = socket(AF_INET, SOCK_DGRAM, 0)
    my_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    
    my_socket.bind(('127.0.0.1', 9000))
    while True:
        data, sender_address = my_socket.recvfrom(4096)
        message = data.decode('utf-8')
        
        if message == "SHUTDOWN":
            print("[UDP Server] Shutdown signal received. Closing.")
            break
            
        print(f"[UDP Server] Received data from {sender_address}: {message}")
        
    my_socket.close()

def run_udp_sender():
    print("[UDP Sender] Preparing to transmit...")
    my_socket_sender = socket(AF_INET, SOCK_DGRAM, 0)
    
    messages = [b"hi there UDP world 1", b"hi there UDP world 2", b"hi there UDP world 3"]
    
    for msg in messages:
        # Simulate unpredictable processing/network lag before sending
        time.sleep(random.uniform(0.01, 0.05)) 
        my_socket_sender.sendto(msg, ('127.0.0.1', 9000))
        
    my_socket_sender.sendto(b"SHUTDOWN", ('127.0.0.1', 9000))
    my_socket_sender.close()
    print("[UDP Sender] Packet transmitted and socket closed.")


async def main():
    loop = asyncio.get_running_loop()
    if os.getenv("UDP") is not None:
        server_task = loop.run_in_executor(None, run_udp_server)
        sender_task = loop.run_in_executor(None, run_udp_sender)
        await asyncio.gather(server_task, sender_task)
    else:
        server_task = loop.run_in_executor(None, run_server)
        await asyncio.sleep(0.1)
        sender_task = loop.run_in_executor(None, run_sender)
        await asyncio.gather(server_task, sender_task)

if __name__ == "__main__":
    asyncio.run(main())
