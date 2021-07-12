import pygame
import numpy as np

class Controls():
    def __init__(self,game):
        self.game=game
        self.input=None
        self.mouse=[0,0]
        self.keys=None
        self.rel=[0,0]
        self.get_controls()
        self.data=self.controls_to_data
        
    def get_controls(self):
        self.keys=pygame.key.get_pressed()
        self.input=pygame.mouse.get_pressed()
        self.rel=pygame.mouse.get_rel()
        self.mouse=pygame.mouse.get_pos()
        
    def controls_to_data(self):
        angle=0
        if self.game.player.pid in self.game.entity_manager.entities:
            self.game.entity_manager.entities[self.game.player.pid].angle-=self.rel[0]/1000.
            angle=self.game.entity_manager.entities[self.game.player.pid].angle

        self.data=':'.join([str(i) for i in [
                self.keys[pygame.K_w],
                self.keys[pygame.K_a],
                self.keys[pygame.K_s],
                self.keys[pygame.K_d],
                int(self.input[0]),
                int(1000*angle)
                ]
            ])
        return self.data
