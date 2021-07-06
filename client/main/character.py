from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

class Character():
    def __init__(self,game, pid, x, y, vx, vy, angle):
        self.game=game
        self.pid=pid
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.angle=angle
        self.r=10
        print(self.game.player.pid, self.pid, type(self.game.player.pid), type(self.pid))
        if self.game.player.pid==self.pid:
            self.colour=(0,0,255,255)
        else:
            self.colour=(255,255,255,255)
        self.sprite=pygame.Surface((2*self.r, 2*self.r), flags=pygame.SRCALPHA)
        self.sprite.fill((255,255,255,0))
        pygame.draw.circle(self.sprite,self.colour,(self.r,self.r),self.r)
        
        self.sprite_size=self.sprite.get_size()
        
    def update(self):
        pass
        
    def draw(self):
        #dx=self.x-self.game.camera.x
        #dy=self.y-self.game.camera.y
        #self.game.screen.blit(self.sprite, (
        #    dx*self.game.camera.cangle+dy*self.game.camera.sangle+self.game.screen.width/2-self.sprite_size[0]/2+self.game.camera.x_shift,
        #    -dx*self.game.camera.sangle+dy*self.game.camera.cangle+self.game.screen.height/2-self.sprite_size[1]/2+self.game.camera.y_shift
        #    )
        #)
        glBegin(GL_QUADS)
        glVertex3fv((self.x-10,self.y-10,0))
        glVertex3fv((self.x-10,self.y+10,0))
        glVertex3fv((self.x+10,self.y+10,0))
        glVertex3fv((self.x+10,self.y-10,0))
        glEnd()
        
    def set_pid(self,pid):
        self.pid=pid
