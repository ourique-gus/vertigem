import pygame

class Camera():
    def __init__(self,game,x=0, y=0):
        self.game=game
        self.x=x
        self.y=y
        
    def update(self):
        if hasattr(self.game,'player') and self.game.player.pid in self.game.entities:
            self.x=self.game.entities[self.game.player.pid].x
            self.y=self.game.entities[self.game.player.pid].y
