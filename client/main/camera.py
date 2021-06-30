import pygame

class Camera():
    def __init__(self,game,x=0, y=0):
        self.game=game
        self.x=x
        self.y=y
        
    def update(self):
        self.x=self.game.player.x
        self.y=self.game.player.y
