import pygame

class Projectile():
    def __init__(self,game, pid, x, y, theta):
        self.game=game
        self.pid=pid
        self.x=x
        self.y=y
        self.theta=theta
        self.r=5
        self.colour=(255,0,0,255)
        self.sprite=pygame.Surface((2*self.r, 2*self.r), flags=pygame.SRCALPHA)
        self.sprite.fill((255,255,255,0))
        pygame.draw.circle(self.sprite,self.colour,(self.r,self.r),self.r)
        
        self.sprite_size=self.sprite.get_size()
        
    def update(self):
        pass
        
    def draw(self):
        dx=self.x-self.game.camera.x
        dy=self.y-self.game.camera.y
        self.game.screen.blit(self.sprite, (
            dx*self.game.camera.cangle+dy*self.game.camera.sangle+self.game.screen.width/2-self.sprite_size[0]/2,
            -dx*self.game.camera.sangle+dy*self.game.camera.cangle+self.game.screen.height/2-self.sprite_size[1]/2
            )
        )
        
    def set_pid(self,pid):
        self.pid=pid
