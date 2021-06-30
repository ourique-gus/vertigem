import pygame
import datetime
from main.networking import Networking
from main.controls import Controls
from main.player import Player
from main.camera import Camera
from main.screen import Screen
from main.character import Character

class Game():
    def __init__(self):
        self.ip='127.0.0.1'
        self.port=7777
        self.tps=30
        self.dt=1/self.tps
        self.is_running=False
        
        self.screen_width=1366
        self.screen_height=768
        
        self.connection_status = self.connect_to_server()
        if self.connection_status:
            self.start_game()
        
    def connect_to_server(self):
        self.print_log('Connecting to server...')
        self.networking=Networking(self, self.ip, self.port)
        connection_status = self.networking.connect()
        if connection_status:
            self.print_log('Connected to the server')
        else:
            self.print_log('Failed to connect to the server')
        return connection_status
        
    def start_game(self):
        self.print_log('>> Game started <<')
        
        self.clock=pygame.time.Clock()
        self.screen=Screen(self,self.screen_width, self.screen_height)
        self.controls=Controls(self)
        self.player=Player(self, self.networking.player_id)
        
        self.screen.start()        
        self.is_running=True
        
        self.entities={100:Character(self,100,200,300, 0)}
        
        while self.is_running:
            self.clock.tick(self.tps)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            
            
            self.controls.get_controls()
            self.controls.controls_to_data()
            
            data=self.networking.send(self.controls.data)
            
            self.screen.update()
            
    def get_now(self):
        return datetime.datetime.now().strftime("%d/%m/%YT%H:%M:%S")
            
    def print_log(self,msg):
        print ('[{}]: {}'.format(self.get_now(), msg))
