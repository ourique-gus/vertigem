import pygame
import datetime
from OpenGL.GL import *
from OpenGL.GLU import *
from main.networking import Networking
from main.controls import Controls
from main.player import Player
from main.camera import Camera
from main.screen import Screen
from main.model_manager import ModelManager
from main.character import Character
from main.projectile_spawner import ProjectileSpawner
from main.background import Background
from main.collider import Collider
from main.projectile import Projectile
from main.entity_manager import EntityManager


class Game():
    def __init__(self):
        self.tps=60
        self.dt=1/self.tps
        self.is_running=False
        
        self.screen_width=1366
        self.screen_height=768
        
        self.connection_status = self.connect_to_server()
        if self.connection_status:
            self.start_game()
        
    def connect_to_server(self):
        self.print_log('Connecting to server...')
        self.networking=Networking(self)
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
        self.model_manager=ModelManager(self)
        self.camera=Camera(self, 0, 0)
        self.screen.start()        
        self.controls=Controls(self)
        self.player=Player(self, self.networking.player_id)
        
        self.networking.start_client_networking_thread()
        
        self.is_running=True
        
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        
        self.model_manager.load_all_models()
        
        self.entity_manager=EntityManager(self)
        
        self.max_server_pid=8192
        self.background=Background(self,8913,1000,1000,20)
        self.entities={
            8913:self.background,
            8914:Collider(self,8914, -500, 500, -500, -450),
            8915:Collider(self,8915, -500, 500, 450, 500),
            8916:Collider(self,8916, -500, -450, -500, 500),
            8917:Collider(self,8917, 450, 500, -500, 500),
            8918:Collider(self,8918, 250, 300, -150, -100),
            8919:Collider(self,8919, 0, 50, -500, 0),
            8920:Collider(self,8920, -350, -300, -100, -50),
            8921:Collider(self,8921, -200, 200, 200, 250),
        }
        
        while self.is_running:
            try:
                self.clock.tick(self.tps)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                        self.is_running = False
                
                self.entity_manager.update_entities()
                self.controls.get_controls()
                self.controls.controls_to_data()
                self.entity_manager.set_entities_data()
                self.camera.update()            
                
                self.screen.update()
            except (KeyboardInterrupt, SystemExit):
                self.is_running=False
            
    def get_now(self):
        return datetime.datetime.now().strftime("%d/%m/%YT%H:%M:%S")
            
    def print_log(self,msg):
        print ('[{}]: {}'.format(self.get_now(), msg))
