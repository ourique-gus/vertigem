from main.info_manager import InfoManager
from main.event_manager import EventManager
from main.character import Character
from main.projectile_spawner import ProjectileSpawner
from main.background import Background
from main.collider import Collider
from main.projectile import Projectile
import numpy as np
import pygame
import os

class EntityManager():
    def __init__(self,game):
        self.game=game
        self.entities={
            8914:Collider(self.game,8914, -500, 500, -500, -450),
            8915:Collider(self.game,8915, -500, 500, 450, 500),
            8916:Collider(self.game,8916, -500, -450, -500, 500),
            8917:Collider(self.game,8917, 450, 500, -500, 500),
            8918:Collider(self.game,8918, 250, 300, -150, -100),
            8919:Collider(self.game,8919, 0, 50, -500, 0),
            8920:Collider(self.game,8920, -350, -300, -100, -50),
            8921:Collider(self.game,8921, -200, 200, 200, 250),
        }
        self.max_server_pid=8192

        self.kind_from_to={
            0:InfoManager,
            1:EventManager,
            8:Character,
            9:Projectile,
            10:ProjectileSpawner,
            }        
        
    def update_entities(self):
        ents=[ent for ent in self.entities]
        for ent in ents:
            if hasattr(self.entities[ent],'remove') and self.entities[ent].remove:
                self.entities.pop(ent)
            elif hasattr(self.entities[ent],'update'):
                self.entities[ent].update()
        ents=[ent for ent in self.entities]
        
    def spawn_entity(self, entity, *parameters):
        pid=self.max_server_pid+np.random.randint(65536)
        while pid in self.entities:
            pid=self.max_server_pid+np.random.randint(65536)
        self.entities[pid]=entity(self.game,pid, *parameters)
            
    def set_entities_data(self):
        data=self.game.networking.data
        if data and len(data):
            pid_list=set()
            pid_data=data.split(',')
            for var in pid_data:
                var_split=var.split(':')
                pid=int(var_split[0])
                pid_list.add(pid)
                kind=int(var_split[1])
                if not pid in self.entities:
                    self.entities[pid]=self.kind_from_to[kind](self.game,pid)
                if hasattr(self.entities[pid],'set_data'):
                    self.entities[pid].set_data(var)
            for ent in self.entities:
                if not ent in pid_list and ent <= self.max_server_pid:
                    self.entities[ent].remove=True
