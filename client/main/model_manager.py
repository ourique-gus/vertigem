from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.arrays import vbo   
import numpy as np
import pygame
import os


class ModelManager():
    def __init__(self,game):
        self.game=game
        self.model_path_list={
            'ship':{'model':['models', 'ship.npz'], 'texture':['models', 'ship.png'] },
            'cube':{'model':['models', 'cube.npz'], 'texture':['models', 'cube.png'] },
            'projectile':{'model':['models', 'projectile.npz'], 'texture':['models', 'projectile.png'] },
            'wall':{'model':['models', 'wall.npz'], 'texture':['models', 'wall.png'] },
        }
        self.t3v1=np.array([0,0,0]).astype(float)
        self.t3v3rz=np.array([[0,0,0],[0,0,0],[0,0,1]]).astype(float)
        
        self.models={}
        self.textures={}
        self.vbos={}
        
    def add_model_path(self, model_name,model_path, texture_path):
        m_path=model_path.split('/')
        if len(m_path) == 1:
            m_path=m_path.split('\\')
        t_path=texture_path.split('/')
        if len(t_path) == 1:
            t_path=t_path.split('\\')
        self.model_path_list[model_name]['model']=m_path
        self.model_path_list[model_name]['texture']=t_path
        
    def load_model(self,model_name):
        m_path=os.path.join(*self.model_path_list[model_name]['model'])
        t_path=os.path.join(*self.model_path_list[model_name]['texture'])
        model=np.load(m_path)
        texture=pygame.image.load(t_path)
        self.models[model_name]={'model':model, 'texture':texture}
        self.textures[model_name]=self.bind_texture(texture)
        self.vbos[model_name]=self.get_vbos(model)
        
    def load_all_models(self):
        for model in self.model_path_list:
            self.load_model(model)
            
    def get_vbos(self, model):
        vertices=model['vertices']
        normals=model['normals']
        faces=model['faces']
        uv=model['uv']
        model=np.require(vertices[faces].ravel(),np.float32,'F')
        model_len=len(model)
        model_vbo=vbo.VBO(model)
        
        normals=np.require(normals[faces].ravel(),np.float32,'F')
        normals_len=len(normals)
        normals_vbo=vbo.VBO(normals)
        
        uv = np.require(uv.ravel(),np.float32,'F')
        uv_len=len(uv)
        uv_vbo=vbo.VBO(uv)
        
        return {'model':model_vbo, 'normals':normals_vbo, 'uv':uv_vbo,
            'model_len':model_len, 'normals_len':normals_len, 'uv_len':uv_len,
            'vertices_a':vertices, 'normals_a':normals, 'faces_a':faces, 'uv_a':uv}
            
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
