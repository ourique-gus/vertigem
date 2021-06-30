import pygame

class Controls():
    def __init__(self,game):
        self.game=game
        self.input=None
        self.mouse=None
        self.keys=None
        
    def get_controls(self):
        self.keys=pygame.key.get_pressed()
        self.input=pygame.mouse.get_pressed()
        self.mouse=pygame.mouse.get_position()
