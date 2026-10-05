import socketserver
import threading

class MyRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        echo_msg = data.decode("utf-8")
        print(f"Received: {echo_msg}")

class MyServer(socketserver.TCPServer):
    def __init__(self, server_address, handler_class=MyRequestHandler):
        print("Server initialised")
        socketserver.TCPServer.__init__(self, server_address, handler_class)

    def serve_forever(self):
        print("Listening for requests...")
        while True:
            self.handle_request()

    def handle_request(self):
        return socketserver.TCPServer.handle_request(self)

    def server_close(self):
        print("Server shutdown")
        return socketserver.TCPServer.server_close(self)

if __name__ == '__main__':
    import socket
    import threading

    ip_address = ('localhost', 8000)
    with MyServer(ip_address, MyRequestHandler) as my_server:
        ip, port = my_server.server_address
        print(f"IP: {ip} is listening on PORT: {port}")
        my_server.serve_forever()
