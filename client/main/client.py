import pygame
from main.networking import Networking
import datetime

class Client():
    def __init__(self):
        self.ip='127.0.0.1'
        self.port=7777
        self.tps=30
        self.dt=1/self.tps
        self.is_running=False
        
        self.connection_status = self.connect_to_server()
        if self.connection_status:
            self.start_client()
        
    def connect_to_server(self):
        self.print_log('Connecting to server...')
        self.networking=Networking(self, self.ip, self.port)
        connection_status = self.networking.connect()
        if connection_status:
            self.print_log('Connected to the server')
        else:
            self.print_log('Failed to connect to the server')
        return connection_status
        
    def start_client(self):
        self.print_log('>> Client started')
        self.clock=pygame.time.Clock()
        self.is_running=True
        data=None
        send=0
        
        while self.is_running:
            self.clock.tick(self.tps)
            send=str(float(send)+1)
            self.print_log("Received: " + str(data) + ", Sending : " + str(send))
            data=self.networking.send(send)
            
    def get_now(self):
        return datetime.datetime.now().strftime("%d/%m/%YT%H:%M:%S")
            
    def print_log(self,msg):
        print ('[{}]: {}'.format(self.get_now(), msg))
