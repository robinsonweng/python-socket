import socket
import time

IP = "localhost"
PORT = 8000
TEXT_ENCODE = "utf-8"

def get(path):
    request = lambda x: f"GET {x} HTTP/1.0"
    with socket.socket() as s:
        s.connect((IP, PORT))
        s.send(request(path).encode(TEXT_ENCODE))


if __name__ == "__main__":
    get("/happy")
    get("/sad")
    get("/sad")
    get("/sad")