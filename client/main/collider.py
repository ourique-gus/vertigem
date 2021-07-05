import numpy as np
import pygame

class Collider():
    def __init__(self,game, pid, xi, xf, yi, yf):
        self.game=game
        self.pid=pid
        self.kind='Collider'
        self.xi=xi
        self.yi=yi
        self.xf=xf
        self.yf=yf
        self.dx=self.xf-self.xi
        self.dy=self.yf-self.yi
        self.colour=(0,170,0,255)
        self.sprite=pygame.Surface((self.dx, self.dy), flags=pygame.SRCALPHA)
        self.sprite.fill(self.colour)
        self.sprite_size=self.sprite.get_size()
        
    def update(self):
        pass
        
    def draw(self):
        dxi=self.xi-self.game.camera.x
        dxf=self.xf-self.game.camera.x
        dyi=self.yi-self.game.camera.y
        dyf=self.yf-self.game.camera.y
        rot=np.vstack([[self.game.camera.cangle, self.game.camera.sangle], [-self.game.camera.sangle, self.game.camera.cangle]]).T
        vec=np.vstack([(dxi,dyi), (dxf,dyi), (dxf,dyf), (dxi,dyf)]).T
        vec_rot=np.dot(rot,vec).T
        vec[:,0]+=self.game.screen.width/2+self.game.camera.x_shift
        vec[:,1]+=self.game.screen.height/2+self.game.camera.y_shift
        
        pygame.draw.polygon(self.game.screen.screen, self.colour, vec_rot)
  
        
