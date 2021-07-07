from OpenGL.GL import *
from OpenGL.GLU import *
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
        
    def get_collision(self, x, y, r):
        xl=-(x+r)+(self.xi)
        xr=+(x-r)-(self.xf)
        yt=(y-r)-(self.yf)
        yb=-(y+r)+(self.yi)
        dx=max([xl,xr])
        dy=max([yt,yb])
        if dx < 0 and dy < 0:
            if dx > dy:
                sign=xl > xr and -1 or 1
                return (-dx*sign, 0)
            else:
                sign=yt > yb and -1 or 1
                return (0,dy*sign)
        
    def update(self):
        pass
        
    def draw(self):
        glColor3f(0.0, 0, 1);
        glBegin(GL_QUADS)
        glVertex3fv((self.xi,self.yi,0))
        glVertex3fv((self.xi,self.yf,0))
        glVertex3fv((self.xf,self.yf,0))
        glVertex3fv((self.xf,self.yi,0))
        glEnd()
        glColor3f(1.0, 1, 1);
        
