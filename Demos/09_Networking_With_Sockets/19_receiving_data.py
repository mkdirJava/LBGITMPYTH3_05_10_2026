# Server code
from socket import socket, AF_INET, SOCK_DGRAM

my_socket = socket(AF_INET, SOCK_DGRAM, 0)
#                           ^^^^^^^^^^^ Note difference for connectionless
ipv4_tuple = '127.0.0.1', 8000
my_socket.bind(ipv4_tuple)
#my_socket.listen()

print(f"Server is listening")

(received_data, address) = my_socket.recvfrom(4096, 0)
print(f"Connection made from: {address}")

decoded_received_data = received_data.decode("utf-8")
print(f"Data received: '{decoded_received_data}'")

my_socket.close()
print("Connection closed")

# 

