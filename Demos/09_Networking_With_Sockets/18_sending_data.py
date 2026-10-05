# Client code
from socket import socket, AF_INET, SOCK_DGRAM

my_socket = socket(AF_INET, SOCK_DGRAM, 0)
#                           ^^^^^^^^^^^ Note difference for connectionless
ipv4_tuple = '127.0.0.1', 8000

my_socket.connect(ipv4_tuple)

msg = b"What hath God wrought!"
print(f"Sending message: {msg}")

# send
#bytest_sent = my_socket.send(msg, 0) # may not all get sent if issue occurs. You must handle partial sends
#sendall
my_socket.sendall(msg, 0) # sends all the data (internally loops until everything is sent). Returns None on success
#send using connectionless socket
my_socket.sendto(msg, 0, ipv4_tuple)

print("message successfully sent")

my_socket.close()
print("Connection closed")
