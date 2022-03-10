import os
import socket

class PeerToPeer:
    def send_message(self, ip, port, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            s.sendall(bytes(message, "utf-8"))

    def send_file(self, ip, port, filepath, filename):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            s.sendall(b"\n".join([open(filepath, "rb").read(), bytes(filename, encoding="utf-8")]))

    def receive_message(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', port))
            s.listen()
            conn, addr = s.accept()
            while True:
                data = conn.recv(1024)
                return data

    def receive_file(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', port))
            s.listen()
            conn, addr = s.accept()
            while True:
                data = conn.recv(10**9).split(b"\n")
                filename = data[-1].decode()
                data = b"\n".join(data[:-1])
                fc = open(filename, "wb")
                fc.write(data)
                return