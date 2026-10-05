from socket import socket, AF_INET6, SOCK_STREAM

my_socket = socket(AF_INET6, SOCK_STREAM, 0)

# (host, port, flowinfo, scopeid)
ipv6_tuple = ("::1", 8000, 0, 0)

my_socket.bind(ipv6_tuple)
my_socket.listen()

print(f"Waiting for connection on port {ipv6_tuple[1]}")

new_socket_object, r_address = my_socket.accept()

print(f"Connection made from: {r_address}")

received_data = new_socket_object.recv(4096)

decoded_received_data = received_data.decode("utf-8")
print(f"Data received: '{decoded_received_data}'")

new_socket_object.close()
my_socket.close()

print("Connection closed")

# Code is best demoed along side 12_simple_socket_based_connection_client-IPv6.py which should be launched first.
# To run with no python client you can use telnet:
# However, telnet needs to be enabled (via Control Panel, "programs and features, Turn windows features on and off, enable Telnet Client " )
# the server app needs to be launched
# from a command prompt enter:
# telnet ::1 8000
# type a single character
# server will print something like: "Data received: 'x'"
# Both telnet and the server app will terminate