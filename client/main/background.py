import numpy as np
import pygame

class Background():
    def __init__(self,game, pid, width, height, num):
        self.game=game
        self.pid=pid
        self.width=width
        self.height=height
        self.num=num
        self.r=3
        self.colour=(127,255,212,255)
        self.sprite=pygame.Surface((2*self.r, 2*self.r), flags=pygame.SRCALPHA)
        self.sprite.fill((255,255,255,0))
        pygame.draw.circle(self.sprite,self.colour,(self.r,self.r),self.r)
        self.sprite_size=self.sprite.get_size()
        self.zorder=-9999
        self.x=(np.random.rand(self.num)-0.5)*self.width
        self.y=(np.random.rand(self.num)-0.5)*self.height
        
    def update(self):
        pass
        
    def draw(self):
        for star in range(self.num):
            self.game.screen.blit(self.sprite, (
                self.x[star]-self.sprite_size[0]/2-self.game.camera.x+self.game.screen.width/2,
                self.y[star]-self.sprite_size[1]/2-self.game.camera.y+self.game.screen.height/2
                )
            )
        
    def set_pid(self,pid):
        self.pid=pid
