# Client code
from socket import socket, AF_INET, SOCK_STREAM

my_socket = socket(AF_INET, SOCK_STREAM, 0)
ipv4_tuple = '127.0.0.1', 8000
try:
    my_socket.connect(ipv4_tuple)

    msg = b"What hath God wrought!"
    print(f"Sending message: {msg}")

    my_socket.send(msg, 0)
    print("message successfully sent")
except Exception as e:
    error = my_socket.connect_ex(ipv4_tuple)
    print(e)
    print(error)
my_socket.close()
print("Connection closed")
