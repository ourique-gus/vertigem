from OpenGL.GL import *
from OpenGL.GLU import *
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
            0:Character,
            1:ProjectileSpawner,
            2:Projectile,
            }        
        
    def update_entities(self):
        ents=[ent for ent in self.entities]
        for ent in ents:
            if hasattr(self.entities[ent],'remove') and self.entities[ent].remove:
                if hasattr(self.entities[ent],'texture_id'):
                    for idv in self.entities[ent].texture_id:
                        glDeleteTextures(1, idv)
                self.entities.pop(ent)
            elif hasattr(self.entities[ent],'update'):
                self.entities[ent].update()
        ents=[ent for ent in self.entities]
            
    def set_entities_data(self):
        data=self.game.networking.data
        print(data)
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
                self.entities[pid].set_data(var)
            for ent in self.entities:
                if not ent in pid_list and ent <= self.max_server_pid:
                    self.entities[ent].remove=True
