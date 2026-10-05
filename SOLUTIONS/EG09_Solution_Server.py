#from __future__ import annotations

import socket
from typing import Dict, Tuple


HOST = "127.0.0.1"
PORT = 5000


def parse_message(message: str) -> Dict[str, str]:
    fields: Dict[str, str] = {}

    for part in message.strip().split("|"):
        if "=" not in part:
            raise ValueError(f"Invalid field format: {part!r}")

        key, value = part.split("=", 1)
        key = key.strip().upper()
        value = value.strip()

        if not key or not value:
            raise ValueError("Empty key or value is not allowed")

        fields[key] = value

    return fields


def mask_pan(pan: str) -> str:
    if len(pan) <= 4:
        return "*" * len(pan)
    return "*" * (len(pan) - 4) + pan[-4:]


def validate_request(fields: Dict[str, str]) -> None:
    required = {"MTI", "PAN", "AMOUNT", "CUR"}
    missing = required - set(fields.keys())
    if missing:
        raise ValueError(f"Missing required fields: {sorted(missing)}")

    if fields["MTI"] != "0100":
        raise ValueError("Only MTI=0100 authorization requests are supported")

    pan = fields["PAN"]
    if not pan.isdigit() or not (12 <= len(pan) <= 19):
        raise ValueError("PAN must be 12 to 19 digits")

    amount = fields["AMOUNT"]
    if not amount.isdigit():
        raise ValueError("AMOUNT must be an integer in minor units")

    currency = fields["CUR"]
    if len(currency) != 3 or not currency.isalpha():
        raise ValueError("CUR must be a 3-letter currency code")


def build_response(response_code: str, message: str) -> str:
    return f"MTI=0110|RC={response_code}|MSG={message}"


def process_request(raw_message: str) -> str:
    fields = parse_message(raw_message)
    validate_request(fields)

    amount = int(fields["AMOUNT"])
    masked_pan = mask_pan(fields["PAN"])

    print(
        "Received transaction:",
        f"PAN={masked_pan}",
        f"AMOUNT={amount}",
        f"CUR={fields['CUR']}",
    )

    if amount < 10_000:
        return build_response("00", "APPROVED")

    return build_response("05", "DECLINED")


def handle_client(conn: socket.socket, addr: Tuple[str, int]) -> None:
    print(f"Connected by {addr}")

    try:
        data = conn.recv(4096)
        if not data:
            print("No data received")
            return

        request = data.decode("utf-8")
        print(f"Raw request: {request}")

        try:
            response = process_request(request)
        except ValueError as exc:
            response = build_response("30", f"FORMAT_ERROR:{exc}")
        except Exception as exc:
            print(f"Unexpected processing error: {exc!r}")
            response = build_response("96", "SYSTEM_ERROR")

        conn.sendall(response.encode("utf-8"))
        print(f"Sent response: {response}")

    except Exception as exc:
        print(f"Connection handling error from {addr}: {exc!r}")
    finally:
        try:
            conn.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        conn.close()
        print("-" * 50)


def run_server() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((HOST, PORT))
        server_sock.listen(5)

        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server_sock.accept()
            handle_client(conn, addr)


if __name__ == "__main__":
    run_server()