from socket import socket, AF_INET, SOCK_STREAM
import ssl

ipv4_tuple = '127.0.0.1', 8000

# Server details, certificate and key
server_hostname = 'qa-example.com'
server_key = r'C:\certs\server.key'
server_cert = r'C:\certs\server.crt'

# Client certificate
client_cert = r'C:\certs\client.crt'

# Create SSL context
my_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
my_context.verify_mode = ssl.CERT_REQUIRED
my_context.load_cert_chain(certfile=server_cert, keyfile=server_key)
my_context.load_verify_locations(cafile=client_cert)
my_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
my_context.set_ciphers('EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH')

# Create normal socket
my_socket = socket(AF_INET, SOCK_STREAM, 0)
my_socket.bind(ipv4_tuple)
my_socket.listen(1)

while True:
    print(f"Waiting for connection on port {ipv4_tuple[1]}")
    new_socket_object, r_address = my_socket.accept()
    print(f"Connection made from: {r_address}")
    ssl_connection = None
    try:
        ssl_connection = my_context.wrap_socket(new_socket_object, server_side=True)
        received_data = ssl_connection.recv(4096, 0)
        if not received_data:
            print("Client closed connection")
            continue
        decoded_received_data = received_data.decode("utf-8")
        print(f"Data received: '{decoded_received_data}'")
    except (ssl.SSLError, ConnectionAbortedError, ConnectionResetError) as e:
        print(f"Connection error: {e}")
    finally:
        if ssl_connection:
            try:
                ssl_connection.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass
            ssl_connection.close()
        new_socket_object.close()

    print("Connection closed")
