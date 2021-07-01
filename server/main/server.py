import pygame
from main.networking import Networking
import datetime

class Server():
    def __init__(self):
        self.ip='192.168.0.57'
        self.port=7777
        self.max_connections=6
        self.tps=30
        self.dt=1/self.tps
        self.is_running=False
        
        
        self.server_status = self.start_networking()
        if self.server_status:
            self.start_server()
        
    def start_networking(self):
        self.print_log('Starting server networking thread...')
        self.networking=Networking(self, self.ip, self.port, self.max_connections)
        server_status = self.networking.setup_networking()
        if server_status:
            self.networking.start_server_networking_thread()
            self.print_log('Server networking thread started.')
        else:
            self.print_log('Failed to bind socket.')
        return server_status
        
    def start_server(self):
        self.print_log('>> Server starter <<')
        self.clock=pygame.time.Clock()
        self.is_running=True
        
        self.entities={}
        
        while self.is_running:
            self.clock.tick(self.tps)
            
            ents={ent for ent in self.entities}
            
            for ent in ents:
                if hasattr(self.entities[ent],'remove') and self.entities[ent].remove:
                    self.entities.pop(ent)
                elif hasattr(self.entities[ent],'update'):
                    self.entities[ent].update()
                
            
    def get_now(self):
        return datetime.datetime.now().strftime("%d/%m/%YT%H:%M:%S")
            
    def print_log(self,msg):
        print ('[{}]: {}'.format(self.get_now(), msg))
