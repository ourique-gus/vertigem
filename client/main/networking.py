import socket
import threading

class Networking:
    def __init__(self, game, ip, port):
        self.game=game
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ip = ip
        self.port = port
        self.addr = (self.ip, self.port)
        
    def connect(self):
        try:
            self.socket.connect(self.addr)
            self.connection_status=bool(self.socket.recv(2048).decode())
            print(self.connection_status)
            return self.connection_status
        except:
            return False

    def send(self, data):
        try:
            self.socket.send(str.encode(data))
            return self.socket.recv(2048).decode()
        except socket.error as e:
            self.game.print_log(str(e))
