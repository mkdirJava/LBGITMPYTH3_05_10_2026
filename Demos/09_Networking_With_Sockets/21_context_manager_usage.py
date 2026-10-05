# Revised Server code
from socket import socket, AF_INET, SOCK_STREAM

ipv4_tuple = '127.0.0.1', 8000

with socket(AF_INET, SOCK_STREAM, 0) as my_socket:

    my_socket.bind(ipv4_tuple)
    my_socket.listen(1)

    print(f"Waiting for connection on port {ipv4_tuple[1]}")
    new_socket_object, r_address = my_socket.accept()

    with new_socket_object:
        print(f"Connection made from: {r_address}")
        while True:
            received_data = new_socket_object.recv(4096, 0)
            if not received_data:
                break
            decoded_received_data = received_data.decode("utf-8")
            print(f"Data received: '{decoded_received_data}'")
            print(decoded_received_data)
    print("Connection closed")
