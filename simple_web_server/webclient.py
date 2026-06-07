"""
A web client that can read data from a given
host and port
"""
import argparse
import socket
from pprint import pprint

def get_response(host: str, port: int) -> None:
    request = (
        "GET / HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(request.encode())

        response = b""
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            response += chunk
    pprint(response.decode())


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", required=False, default=80, type=int)
    args = parser.parse_args()
    get_response(args.host, args.port)
