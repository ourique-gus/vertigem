import socket
import threading
import urllib.request
import time

class Networking:
    def __init__(self, game, ip=None, port=None):
        self.game=game
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ip = not ip and (socket.gethostname()=='brynhildr' and '192.168.0.57' or self.get_server_ip()) or ip
        self.port = not port and 7777 or port
        self.addr = (self.ip, self.port)
        self.player_id=0
        self.data=''
        
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
            exit()
            
    def get_server_ip(self):
        with urllib.request.urlopen('https://gleenusip.herokuapp.com/') as data:
            return data.read().decode("utf-8")
            
    def client_thread(self):
        time.sleep(1)
        while self.game.is_running:
            self.data = self.send(self.game.controls.data)
                        
    def start_client_networking_thread(self):
        self.client_networking_thread=threading.Thread(target=self.client_thread, args=())
        self.client_networking_thread.start()
        
