from socket import socket, AF_INET6, SOCK_STREAM

my_socket = socket(AF_INET6, SOCK_STREAM, 0)

# (host, port, flowinfo, scopeid)
ipv6_tuple = ("::1", 8000, 0, 0)

my_socket.connect(ipv6_tuple)

msg = b"What hath God wrought! (IVp6)"
print(f"Sending message: {msg}")

bytes_sent = my_socket.send(msg)

print(f"{bytes_sent} bytes successfully sent")

my_socket.close()
print("Connection closed")