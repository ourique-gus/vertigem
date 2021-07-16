from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.arrays import vbo
import pygame
import numpy as np

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
        self.cx=0.5*(self.xf+self.xi)
        self.cy=0.5*(self.yf+self.yi)
        self.colour=(0,170,0,255)
        self.sprite=pygame.Surface((self.dx, self.dy), flags=pygame.SRCALPHA)
        self.sprite.fill(self.colour)
        self.sprite_size=self.sprite.get_size()
        
        model_name='wall'
        
        self.vertices=self.game.model_manager.scale(self.game.model_manager.models[model_name]['model']['vertices'],self.dx/2,self.dy/2,50)
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
    
        glLoadIdentity()
        glTranslatef(self.cx,self.cy,50)
        
        glEnable(GL_LIGHTING)
        
        #glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT,(0.2,0.2,0.2,1))
        glMaterialfv(GL_BACK,GL_DIFFUSE,(1,1,1,1))
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
        
