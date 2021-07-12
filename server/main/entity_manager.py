import pygame
import datetime
from main.collider import Collider
from main.character import Character
import numpy as np

class EntityManager():
    def __init__(self,server):
        self.server=server
        self.entities={
            8914:Collider(self,8914, -500, 500, -500, -450),
            8915:Collider(self,8915, -500, 500, 450, 500),
            8916:Collider(self,8916, -500, -450, -500, 500),
            8917:Collider(self,8917, 450, 500, -500, 500),
            8918:Collider(self,8918, 250, 300, -150, -100),
            8919:Collider(self,8919, 0, 50, -500, 0),
            8920:Collider(self,8920, -350, -300, -100, -50),
            8921:Collider(self,8921, -200, 200, 200, 250),
        }
        self.id_range={
            'ping':[0,0],
            'character':[1,256],
            'structure':[256,512],
            'projectile':[512,4096],
            'other':[4096,8192]
        }
        
        self.kind_from_to={
            'Character':0,
            'ProjectileSpawner':1,
            'Projectile':2,
            }
            
        self.event_from_to={
            'None':0,
            }
            
    def update_entities(self):
        ents={ent for ent in self.entities}
        
        for ent in ents:
            if hasattr(self.entities[ent],'remove') and self.entities[ent].remove:
                self.entities.pop(ent)
            elif hasattr(self.entities[ent],'update'):
                self.entities[ent].update()
        
    def get_entities_data(self, pid):
        entity_data = {ent:('%4d:' % ent +self.entities[ent].get_data(pid)).replace(' ','') for ent in self.entities if hasattr(self.entities[ent], 'get_data')}
        return entity_data
