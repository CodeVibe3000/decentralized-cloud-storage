import os

class PeerToPeer:

    def send_file(self, ip, port, file_path):
        os.system(f'cat {file_path} | nc {ip} {str(port)}')

    def send_message(self, ip, port, message):
        os.system(f'echo "{message}" | nc + ip + {str(port)}')

    def receive_file(self, port, output_file):
        os.system(f'nc -l {str(port)} >> {output_file}')

    def receive_message(self, port):
        return os.system("nc -l " + port)


