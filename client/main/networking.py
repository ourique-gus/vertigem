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
        self.player_id=0
        
    def connect(self):
        try:
            self.socket.connect(self.addr)
            self.player_id=self.socket.recv(2048).decode()
            self.connection_status=self.player_id
            return self.connection_status
        except Exception as e:
            print(e)
            return False

    def send(self, data):
        try:
            self.socket.send(str.encode(data))
            return self.socket.recv(2048).decode()
        except socket.error as e:
            self.game.print_log(str(e))
