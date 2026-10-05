# Client code
from socket import socket, AF_INET, SOCK_STREAM

my_socket = socket(AF_INET, SOCK_STREAM, 0)

ipv4_tuple = '127.0.0.1', 8000

my_socket.connect(ipv4_tuple)

msg = b"What hath God wrought!"
print(f"Sending message: {msg}")

# send
bytest_sent = my_socket.send(msg, 0) # may not all get sent if issue occurs. You must handle partial sends

print("message successfully sent")

my_socket.close()
print("Connection closed")
