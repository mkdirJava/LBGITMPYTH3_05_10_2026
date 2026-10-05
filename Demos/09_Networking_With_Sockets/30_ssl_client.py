from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR
import ssl
import time

ipv4_tuple = '127.0.0.1', 8000
# Server details and certificate
server_sni_hostname = 'qa-example.com'
server_cert = r'C:\certs\server.crt'
# Client certificate and key
client_cert = r'C:\certs\client.crt'
client_key = r'C:\certs\client.key'

# Create SSL context
my_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH,
                                        cafile=server_cert)
my_context.load_cert_chain(certfile=client_cert, keyfile=client_key)
# Create normal socket
my_socket = socket(AF_INET, SOCK_STREAM, 0)
# Wrap socket in SSL
ssl_connection = my_context.wrap_socket(my_socket, server_side=False,
                                  server_hostname=server_sni_hostname)

# Connect and transmit
ssl_connection.connect(ipv4_tuple)
msg = b"What hath God wrought!"
print(f"Sending message: {msg}")
ssl_connection.send(msg, 0)
print("message successfully sent")
time.sleep(0.1)   # ← critical to cure race condition
ssl_connection.shutdown(SHUT_RDWR)
ssl_connection.close()
print("Connection closed")
