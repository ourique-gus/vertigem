import pygame
import datetime
from main.networking import Networking
from main.controls import Controls
from main.player import Player
from main.camera import Camera
from main.screen import Screen
from main.character import Character
from main.projectile_spawner import ProjectileSpawner
from main.background import Background
from main.collider import Collider

class Game():
    def __init__(self):
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
        self.controls=Controls(self)
        self.player=Player(self, self.networking.player_id)
        self.camera=Camera(self, 0, 0)
        
        self.screen.start()        
        self.is_running=True
        
        self.kind_from_to={
            0:Character,
            1:ProjectileSpawner,
            }
            
        self.event_from_to={
            0:None,
            }
        
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        
        self.max_server_pid=8192
        self.background=Background(self,8913,1000,1000,1000)
        self.entities={
            8913:self.background,
            #8914:Collider(self,8914, 0, 200, 0, 50)
        }
        
        
        while self.is_running:
            self.clock.tick(self.tps)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            
            ents=[ent for ent in self.entities]
            for ent in ents:
                if hasattr(self.entities[ent],'remove') and self.entities[ent].remove:
                    self.entities.pop(ent)
                elif hasattr(self.entities[ent],'update'):
                    self.entities[ent].update()
            ents=[ent for ent in self.entities]

            self.controls.get_controls()
            self.controls.controls_to_data()
            #pygame.mouse.set_pos(self.screen_width/2, self.screen_height/2)
            
            data=self.networking.send(self.controls.data)
            if data and len(data):
                pid_list=set()
                players=data.split(',')
                for var in players:
                    info=var.split(':')
                    pid=int(info[0])
                    pid_list.add(pid)
                    kind=int(info[1])
                    x=float(info[2])/100
                    y=float(info[3])/100
                    vx=float(info[4])/100
                    vy=float(info[5])/100
                    event=int(info[6])
                    if not pid in self.entities:
                        self.entities[pid]=self.kind_from_to[kind](self,pid,x,y, vx, vy, 0)
                    self.entities[pid].x=x
                    self.entities[pid].y=y
                    self.entities[pid].vx=vx
                    self.entities[pid].vy=vy
                for ent in ents:
                    if not ent in pid_list and ent <= self.max_server_pid:
                        self.entities[ent].remove=True
            self.camera.update()            
            
            self.screen.update()
            
    def get_now(self):
        return datetime.datetime.now().strftime("%d/%m/%YT%H:%M:%S")
            
    def print_log(self,msg):
        print ('[{}]: {}'.format(self.get_now(), msg))
