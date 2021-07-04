import pygame

class Character():
    def __init__(self,game, pid, x, y, theta):
        self.game=game
        self.pid=pid
        self.x=x
        self.y=y
        self.theta=theta
        self.r=10
        print(self.game.player.pid, self.pid, type(self.game.player.pid), type(self.pid))
        if self.game.player.pid==self.pid:
            self.colour=(0,0,255,255)
        else:
            self.colour=(255,255,255,255)
        self.sprite=pygame.Surface((2*self.r, 2*self.r), flags=pygame.SRCALPHA)
        self.sprite.fill((255,255,255,0))
        pygame.draw.circle(self.sprite,self.colour,(self.r,self.r),self.r)
        
    def update(self):
        pass
        
    def draw(self):
        self.game.screen.blit(self.sprite, (self.x,self.y))
        
    def set_pid(self,pid):
        self.pid=pid
