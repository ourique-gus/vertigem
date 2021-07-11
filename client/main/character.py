from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.arrays import vbo
from main.model_transform import ModelTransform
import pygame
import numpy as np

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
        
        model_name='ship'
        
        self.vertices=model_transform.scale(self.game.model_loader.models[model_name]['model']['vertices'],10,10,10)
        self.faces=self.game.model_loader.models[model_name]['model']['faces']
        self.normals=model_transform.normals(self.game.model_loader.models[model_name]['model']['normals'],self.faces)
        self.uv=model_transform.uv(self.game.model_loader.models[model_name]['model']['uv'])
        self.texture_id=[ model_transform.bind_texture(self.game.model_loader.models[model_name]['texture']) ]

        self.model=model_transform.model(self.vertices,self.faces)
        self.model_len=len(self.model)
        self.model_vbo=vbo.VBO(self.model)
        
        self.normals_len=len(self.normals)
        self.normals_vbo=vbo.VBO(self.normals)
        
        self.uv_len=len(self.uv)
        self.uv_vbo=vbo.VBO(self.uv)
        self.tick=0
        
    def update(self):
        pass
        #self.x=self.x+self.vx
        #self.y=self.y+self.vy
        self.tick+=1
        
    def draw(self):

        glLoadIdentity()
        glTranslatef(self.x,self.y,0)
        glRotatef(self.angle*180/np.pi+self.tick,0 , 0, 1)
        
        glEnable(GL_LIGHTING)
        
        #glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT,(0.2,0.2,0.2,1))
        glMaterialfv(GL_FRONT_AND_BACK,GL_DIFFUSE,(1,1,1,1))
        #glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR,(0,0,0,1))
        #glMaterialf(GL_FRONT_AND_BACK,GL_SHININESS,0)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_BLEND)
        glEnable(GL_TEXTURE_2D)
        glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA);
        #glBlendEquation(GL_FUNC_ADD);
        glColor4f(1,1,1,1)
        
        

        
        glEnableClientState(GL_NORMAL_ARRAY)
        glBindTexture(GL_TEXTURE_2D, self.texture_id[0]) 
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glEnableClientState(GL_VERTEX_ARRAY)

        self.uv_vbo.bind()
        glTexCoordPointer(2, GL_FLOAT, 0, self.uv_vbo)
        self.uv_vbo.unbind()
        
        self.normals_vbo.bind()
        glNormalPointer(GL_FLOAT, 0, self.normals_vbo)
        self.normals_vbo.unbind()
        
        """
        self.model_vbo[:] = model_transform.model(
                model_transform.move(
                    #model_transform.rot_z(self.vertices,-self.angle),
                    self.vertices,
                    self.x,self.y,self.z),
                self.faces)
        self.model_vbo.bind()
        """
        self.model_vbo.bind()
        self.model_vbo.implementation.glBufferSubData(self.model_vbo.target, 0, self.model_vbo.data)
        glVertexPointer(3, GL_FLOAT, 0, self.model_vbo)
        self.model_vbo.unbind()
        

        glDrawArrays(GL_TRIANGLES, 0, self.model_len)
       
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_NORMAL_ARRAY)
        
        
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)
        glDisable(GL_BLEND)
        glDisable(GL_TEXTURE_2D)
        
        
        glColor3f(1.0, 1, 1);
        
    def set_pid(self,pid):
        self.pid=pid
