import pygame
import numpy as np

class Controls():
    def __init__(self,game):
        self.game=game
        self.input=None
        self.mouse=None
        self.keys=None
        
    def get_controls(self):
        self.keys=pygame.key.get_pressed()
        self.input=pygame.mouse.get_pressed()
        self.mouse=pygame.mouse.get_pos()
        
    def controls_to_data(self):
        angle=0
        if self.game.player.pid in self.game.entities:
            x=self.game.entities[self.game.player.pid].x
            y=self.game.entities[self.game.player.pid].y
            dx=self.mouse[0]-x
            dy=self.mouse[1]-y
            angle=1000*np.arctan2(dy,dx)
        self.data=':'.join([str(i) for i in [
                self.keys[pygame.K_w],
                self.keys[pygame.K_a],
                self.keys[pygame.K_s],
                self.keys[pygame.K_d],
                int(self.input[0]),
                int(angle)
                ]
            ])
        return self.data
