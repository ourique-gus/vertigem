import pygame
import datetime
from main.collider import Collider
from main.character import Character
from main.info_manager import InfoManager
from main.event_manager import EventManager
import numpy as np

class EntityManager():
    def __init__(self,server):
        self.server=server
        self.info_manager=InfoManager(self.server,0)
        self.event_manager=EventManager(self.server,1)
        self.entities={
            0:self.info_manager,
            1:self.event_manager,
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
            'information':[0,1],
            'events':[1,2],
            'placeholder':[2,8],
            'character':[8,256],
            'structure':[256,512],
            'projectile':[512,4096],
            'other':[4096,8192]
        }
        
        self.kind_from_to={
            'InfoManager':0,
            'EventManager':1,
            'Character':8,
            'Projectile':9,
            'ProjectileSpawner':10,
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
