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
        if self.game.player.pid in self.game.entities:
            #x=self.game.entities[self.game.player.pid].x
            #y=self.game.entities[self.game.player.pid].y
            #dx=self.mouse[0]-x
            #dy=self.mouse[1]-y
            #dx=self.mouse[0]-self.game.screen.width/2
            #dy=self.mouse[1]-self.game.screen.height/2
            #angle=np.arctan2(dy,dx)
            self.game.entities[self.game.player.pid].angle-=self.rel[0]/1000.
            angle=self.game.entities[self.game.player.pid].angle

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
