import pygame
import datetime
from main.networking import Networking
from main.collider import Collider
from main.character import Character
from main.entity_manager import EntityManager

class Server():
    def __init__(self):
        self.ip='192.168.0.57'
        self.port=7777
        self.max_connections=6
        self.tps=60
        self.dt=1/self.tps
        self.is_running=True
        
        
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
        self.entity_manager=EntityManager(self)
            
        while self.is_running:
        
            try:
                self.clock.tick(self.tps)
            
                self.entity_manager.update_entities()
            except (KeyboardInterrupt, SystemExit):
                self.is_running=False
            
    def get_now(self):
        return datetime.datetime.now().strftime("%d/%m/%YT%H:%M:%S")
            
    def print_log(self,msg):
        print ('[{}]: {}'.format(self.get_now(), msg))
