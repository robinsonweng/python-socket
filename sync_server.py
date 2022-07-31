import re
import time
import socket


IP = "localhost"
PORT = 8000 
MAX_CONN = 1
MAX_RECV_SIZE = 1024 
SOCKET_TIMEOUT = 0
TEXT_ENCODE = "UTF-8"



def server():
    with socket.socket() as s:
        s.bind((IP, PORT))
        s.listen(1)
    
        while True:
            client, addr = s.accept()
            chunks = []
            with client:
                start = time.time()
                while True:
                    chunk = client.recv(MAX_RECV_SIZE)
                    if chunk:
                        chunks.append(chunk)
                    else:
                        body = (b''.join(chunks)).decode(TEXT_ENCODE)
                        print(body.split("\n")[0])
                        break
                print(f"回應花費: {time.time() - start}s")

if __name__ == "__main__":
    server()