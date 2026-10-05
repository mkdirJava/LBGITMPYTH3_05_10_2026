#from __future__ import annotations
import socket


HOST = "127.0.0.1"
PORT = 5000

def build_auth_request(pan: str, amount: int, currency: str) -> str:
    """
    Build a simple authorization request message.

    amount is in minor units, e.g. pence:
    950 = 9.50 GBP

    MTI 0100 = Authorisation Request ("can I charge?")
    """
    return f"MTI=0100|PAN={pan}|AMOUNT={amount}|CUR={currency}"


def send_request(message: str) -> str:
    """
    Send a sample request to the server and return the response
    received.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(message.encode("utf-8"))

        response = sock.recv(4096)

    return response.decode("utf-8")


def main() -> None:
    """
    Simulate a request, send it and print response.
    """
    request = build_auth_request(
        pan="4111111111111111",      # Simulate card
        amount=10075,
        currency="GBP",
    )

    print(f"Sending request: {request}")
    response = send_request(request)
    print(f"Received response: {response}")


if __name__ == "__main__":
    main()
    