from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.arrays import vbo
import pygame
import numpy as np


class Character():
    def __init__(self,game, pid, x=0, y=0, vx=0, vy=0, angle=0):
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
        
        self.vertices=self.game.model_manager.scale(self.game.model_manager.models[model_name]['model']['vertices'],10,10,3)
        self.faces=self.game.model_manager.models[model_name]['model']['faces']
        self.normals=self.game.model_manager.normals(self.game.model_manager.models[model_name]['model']['normals'],self.faces)
        self.uv=self.game.model_manager.uv(self.game.model_manager.models[model_name]['model']['uv'])
        self.texture_id=[ self.game.model_manager.bind_texture(self.game.model_manager.models[model_name]['texture']) ]

        self.model=self.game.model_manager.model(self.vertices,self.faces)
        self.model_len=len(self.model)
        self.model_vbo=vbo.VBO(self.model)
        
        self.normals_len=len(self.normals)
        self.normals_vbo=vbo.VBO(self.normals)
        
        self.uv_len=len(self.uv)
        self.uv_vbo=vbo.VBO(self.uv)
        self.tick=0
        
    def update(self):
        self.x=self.x+self.vx
        self.y=self.y+self.vy
        self.tick+=1
        
    def set_data(self, data):
        print(data)
        data_int=list(map(int,data.split(':')))
        self.x=data_int[2]/1000.
        self.y=data_int[3]/1000.
        self.vx=data_int[4]/100.
        self.vy=data_int[5]/100.
        
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
