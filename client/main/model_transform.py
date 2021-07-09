from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.arrays import vbo
import numpy as np
import pygame
import os

class ModelTransform():
    def __init__(self):
        
        self.t3v1=np.array([0,0,0]).astype(float)
        self.t3v3rz=np.array([[0,0,0],[0,0,0],[0,0,1]]).astype(float)
        
    def model(self,vertices,faces):
        return np.require(vertices[faces].ravel(),np.float32,'F')
        
    def normals(self,normals,faces):
        return np.require(normals[faces].ravel(),np.float32,'F')
        
    def uv(self,uv):
        return np.require(uv.ravel(),np.float32,'F')
        
    def bind_texture(self,texture):
        textureTranspose=pygame.transform.flip(texture,False,False)
        textureData = pygame.image.tostring(textureTranspose, "RGBA", 1)
        width = textureTranspose.get_width()
        height = textureTranspose.get_height()

        glEnable(GL_TEXTURE_2D)
        idv = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, idv)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glDisable(GL_TEXTURE_2D)
        
        return idv
        
    def scale(self,vertices,sx,sy,sz):
        self.t3v1[0]=sx
        self.t3v1[1]=sy
        self.t3v1[2]=sz
        return self.t3v1*vertices
        
    def rot_z(self,vertices,angle):
        cangle=np.cos(angle)
        sangle=np.sin(angle)
        self.t3v3rz[0,0]=cangle
        self.t3v3rz[1,1]=cangle
        self.t3v3rz[0,1]=-sangle
        self.t3v3rz[1,0]=sangle
        return np.dot(vertices,self.t3v3rz)
        
    def move(self,vertices,sx,sy,sz):
        self.t3v1[0]=sx
        self.t3v1[1]=sy
        self.t3v1[2]=sz
        return self.t3v1+vertices
