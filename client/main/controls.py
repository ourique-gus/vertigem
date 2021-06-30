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
        self.mouse=pygame.mouse.get_pos()
        
    def controls_to_data(self):
        self.data=':'.join([str(i) for i in [self.keys[pygame.K_w], self.keys[pygame.K_a], self.keys[pygame.K_s], self.keys[pygame.K_d]]])
        return self.data
