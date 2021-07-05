import numpy as np
import pygame

class Camera():
    def __init__(self,game,x=0, y=0):
        self.game=game
        self.x=x
        self.y=y
        self.angle=0
        self.cangle=1
        self.sangle=0
        
    def update(self):
        if hasattr(self.game,'player') and self.game.player.pid in self.game.entities:
            self.x=self.game.entities[self.game.player.pid].x
            self.y=self.game.entities[self.game.player.pid].y
            self.angle=self.game.entities[self.game.player.pid].angle
            self.cangle=np.cos(self.angle)
            self.sangle=np.sin(self.angle)
