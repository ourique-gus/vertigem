from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.arrays import vbo
import pygame
from main.model_transform import ModelTransform

model_transform=ModelTransform()

class Character():
    def __init__(self,game, pid, x, y, vx, vy, angle):
        self.game=game
        self.pid=pid
        self.kind='Character'
        self.x=x
        self.y=y
        self.z=10
        self.vx=vx
        self.vy=vy
        self.angle=angle
        self.r=10
        if self.game.player.pid==self.pid:
            self.colour=(0,0,255,255)
        else:
            self.colour=(255,255,255,255)
        
        self.vertices=model_transform.scale(self.game.model_loader.models['ship']['vertices'],10,10,10)
        self.faces=self.game.model_loader.models['ship']['faces']
        self.model=model_transform.model(self.vertices,self.faces)
        self.model_len=len(self.model)
        self.vbo=vbo.VBO(self.model)
        
    def update(self):
        self.x=self.x+self.vx
        self.y=self.y+self.vy
        
    def draw(self):
        
        glEnable(GL_LIGHTING)
        
        #glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT,(0.2,0.2,0.2,1))
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(1,0.0,0.8,1))
        #glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR,(0,0,0,1))
        #glMaterialf(GL_FRONT_AND_BACK,GL_SHININESS,0)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA);
        #glBlendEquation(GL_FUNC_ADD);
        glColor4f(0.5,0.5,0.5,1)
        
        glNormal3fv((0,0,1))
        glEnableClientState(GL_VERTEX_ARRAY)
        self.vbo[:] = model_transform.model(
                model_transform.move(
                    #model_transform.rot_z(self.vertices,-self.angle),
                    self.vertices,
                    self.x,self.y,self.z),
                self.faces)
        self.vbo.bind()
        self.vbo.implementation.glBufferSubData(self.vbo.target, 0, self.vbo.data)
        glVertexPointer(3, GL_FLOAT, 0, self.vbo)
        glDrawArrays(GL_TRIANGLES, 0, self.model_len)
        self.vbo.unbind()
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisable(GL_COLOR_MATERIAL)
        glDisable(GL_LIGHTING)
        glDisable(GL_BLEND)
        
        glColor3f(1.0, 1, 1);
        
    def set_pid(self,pid):
        self.pid=pid
