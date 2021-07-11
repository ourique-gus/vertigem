from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import pygame

def IdentityMat44():
    return np.matrix(np.identity(4), copy=False, dtype='float32')

class Camera():
    def __init__(self,game,x=0, y=0):
        self.game=game
        self.x=x
        self.y=y
        self.z=100
        self.angle=0
        self.cangle=1
        self.sangle=0
        self.x_shift=0
        self.y_shift=300
        self.fov=90
        self.min_dist=0.1
        self.max_dist=1000
        self.ratio=self.game.screen_width/self.game.screen_height
        
        
    def update(self):
        if hasattr(self.game,'player') and self.game.player.pid in self.game.entities:
            self.x=(5*self.x+self.game.entities[self.game.player.pid].x)/6.
            self.y=(5*self.y+self.game.entities[self.game.player.pid].y)/6.
            self.angle=self.game.entities[self.game.player.pid].angle
            self.cangle=np.cos(self.angle)
            self.sangle=np.sin(self.angle)
            
    def place_camera(self):
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective( self.fov , self.ratio, self.min_dist , self.max_dist )
        gluLookAt(self.x,self.y,self.z,self.x+0.9*self.z*self.cangle,self.y+0.9*self.z*self.sangle,0,self.cangle,self.sangle,0)
        
        

        #glRotatef(180,1 , 0, 0)
        #glTranslatef(-self.x,-self.y,self.z)
        #gluPerspective( self.fov , self.ratio, self.min_dist , self.max_dist )
