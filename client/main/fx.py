from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.arrays import vbo
import pygame
import numpy as np


class RandomCube():
    def __init__(self,game, pid, x=0, y=0, vx=0, vy=0, vz=0, s=1):
        self.game=game
        self.pid=pid
        self.kind='RandomCube'
        self.x=x
        self.y=y
        self.z=0
        self.vx=vx
        self.vy=vy
        self.vz=vz
        self.size=2
        self.dsize=0.1
        self.rot=np.random.rand(3)*360
        self.drot=60
        self.tick=0
        self.r=1
        
        model_name='cube'
       
        self.vbo=self.game.model_manager.vbos[model_name]
        self.texture_id=[self.game.model_manager.textures[model_name]]
        
    def look_for_collider(self):
        for ent in self.game.entity_manager.entities:
            if self.game.entity_manager.entities[ent].kind=='Collider':
                collision=self.game.entity_manager.entities[ent].get_collision(self.x,self.y,self.r)
                if collision:
                    return True
        
    def update(self):
        self.tick+=1
        
        self.x+=self.vx
        self.y+=self.vy
        self.z+=self.vz
        
        self.rot+=(np.random.rand(3)-0.5)*self.drot
        self.size-=np.random.rand()*self.dsize
        
        if self.tick > 60 or self.size <= 0:
            self.remove=True
            
        if self.look_for_collider():
            self.remove=True
        
    def draw(self):
        glLoadIdentity()
        glTranslatef(self.x,self.y,self.z)
        glRotatef(*self.rot,1)
        glScalef(self.size,self.size,self.size)
        
        glEnable(GL_LIGHTING)
        
        glMaterialfv(GL_FRONT_AND_BACK,GL_DIFFUSE,(1,1,1,1))
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_BLEND)
        glEnable(GL_TEXTURE_2D)
        glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA);
        glColor4f(1,1,1,1)
        
        

        
        glEnableClientState(GL_NORMAL_ARRAY)
        glBindTexture(GL_TEXTURE_2D, self.texture_id[0]) 
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glEnableClientState(GL_VERTEX_ARRAY)

        self.vbo['uv'].bind()
        glTexCoordPointer(2, GL_FLOAT, 0, self.vbo['uv'])
        self.vbo['uv'].unbind()
        self.vbo['normals'].bind()
        glNormalPointer(GL_FLOAT, 0, self.vbo['normals'])
        self.vbo['normals'].unbind()
        
        self.vbo['model'].bind()
        glVertexPointer(3, GL_FLOAT, 0, self.vbo['model'])
        self.vbo['model'].unbind()
        

        glDrawArrays(GL_TRIANGLES, 0, self.vbo['model_len'])
       
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_NORMAL_ARRAY)
        
        
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)
        glDisable(GL_BLEND)
        glDisable(GL_TEXTURE_2D)
        
        glColor3f(1.0, 1, 1);
        
class RedCube():
    def __init__(self,game, pid, x=0, y=0, vx=0, vy=0, vz=0, s=1):
        self.game=game
        self.pid=pid
        self.kind='RandomCube'
        self.x=x
        self.y=y
        self.z=0
        self.vx=vx
        self.vy=vy
        self.vz=vz
        self.size=2
        self.dsize=0.1
        self.rot=np.random.rand(3)*360
        self.drot=60
        self.tick=0
        self.r=1
        
        model_name='redcube'
       
        self.vbo=self.game.model_manager.vbos[model_name]
        self.texture_id=[self.game.model_manager.textures[model_name]]
        
    def look_for_collider(self):
        for ent in self.game.entity_manager.entities:
            if self.game.entity_manager.entities[ent].kind=='Collider':
                collision=self.game.entity_manager.entities[ent].get_collision(self.x,self.y,self.r)
                if collision:
                    return True
        
    def update(self):
        self.tick+=1
        
        self.x+=self.vx
        self.y+=self.vy
        self.z+=self.vz
        
        self.rot+=(np.random.rand(3)-0.5)*self.drot
        self.size-=np.random.rand()*self.dsize
        
        if self.tick > 60 or self.size <= 0:
            self.remove=True
            
        if self.look_for_collider():
            self.remove=True
        
    def draw(self):
        glLoadIdentity()
        glTranslatef(self.x,self.y,self.z)
        glRotatef(*self.rot,1)
        glScalef(self.size,self.size,self.size)
        
        glEnable(GL_LIGHTING)
        
        glMaterialfv(GL_FRONT_AND_BACK,GL_DIFFUSE,(1,1,1,1))
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_BLEND)
        glEnable(GL_TEXTURE_2D)
        glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA);
        glColor4f(1,1,1,1)
        
        

        
        glEnableClientState(GL_NORMAL_ARRAY)
        glBindTexture(GL_TEXTURE_2D, self.texture_id[0]) 
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glEnableClientState(GL_VERTEX_ARRAY)

        self.vbo['uv'].bind()
        glTexCoordPointer(2, GL_FLOAT, 0, self.vbo['uv'])
        self.vbo['uv'].unbind()
        self.vbo['normals'].bind()
        glNormalPointer(GL_FLOAT, 0, self.vbo['normals'])
        self.vbo['normals'].unbind()
        
        self.vbo['model'].bind()
        glVertexPointer(3, GL_FLOAT, 0, self.vbo['model'])
        self.vbo['model'].unbind()
        

        glDrawArrays(GL_TRIANGLES, 0, self.vbo['model_len'])
       
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_NORMAL_ARRAY)
        
        
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)
        glDisable(GL_BLEND)
        glDisable(GL_TEXTURE_2D)
        
        glColor3f(1.0, 1, 1);
        
