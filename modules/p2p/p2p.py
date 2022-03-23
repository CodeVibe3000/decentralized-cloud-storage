import os
import socket
import time

class PeerToPeer:

    def __init__(self, sport):
        self.sport = sport

    def send_message(self, ip, port, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            s.sendall(bytes(message, "utf-8"))

    def send_file(self, ip, port, filepath, filename, fileorshare="file"):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            s.sendall(b"\n".join([bytes(fileorshare, 'utf-8'), bytes(self.sport), open(filepath, "rb").read(), bytes(filename, 'utf-8')]))

    def receive_message(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('0.0.0.0', self.sport))
            s.listen() 
            while True:
                conn, addr = s.accept()
                data = conn.recv(1024)
                return data

    def receive_file(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('0.0.0.0', self.sport))
            s.listen()
            while True:
                conn, addr = s.accept()
                data = conn.recv(10**9).split(b"\n")
                filename = data[-1].decode()
                if(data[0] != b"file"):
                    return None
                data = b"\n".join(data[2:-1])
                return data

    def request_file(self, ip, port, filename):
        # Send token for file to verify ownership
        self.send_message(ip, port, "\n".join(["request_file", str(self.sport), filename]))
        data = (self.receive_file())
        # Put file in correct place
        if data is not None:
            with open("req_"+filename, "wb") as f:
                f.write(data)


    def listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('127.0.0.1', self.sport))
            s.listen()
            while True:
                conn, addr = s.accept()
                data = conn.recv(10**9).split(b"\n")
                if(data != [b""]):
                    if data[0] == b"request_file":
                        source_port = int(data[1].decode())
                        filename = data[2].decode()
                        # Add search for file in directory and add security to make sure user owns the file being sent
                        self.send_file(addr[0], source_port, filename, filename)
                    elif data[0] == b"share":
                        share = b"\n".join(data[2:-1])
                        filename = data[-1].decode()
                        if data is not None:
                            with open("rec_"+filename, "wb") as f:
                                f.write(share) 
                        