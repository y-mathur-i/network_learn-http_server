"""
Server which listens on a specific port
and responds with a single string
"""
import socket
import argparse

def start_server(port: int) -> None:
    print(f"Listening on port {port}")
    data = b"this is data from server"

    # create a socket
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_.bind(("localhost", port))
    socket_.listen(1)
    while True:
        print("looking for connection")
        connection, client_address = socket_.accept()
        print(f"Connection created on address: {client_address}")
        try:
            while True:
                _ = connection.recv(4096)
                print("Data received: ", data)  
                if _:
                    # send the data back
                    connection.send(data)
                    break
                else:
                    print("No data from connection")
                    break
        finally:
            # close connection in end
            connection.close()

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", required=True, type=int)
    args = parser.parse_args()
    start_server(args.port)


