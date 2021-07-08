from OpenGL.arrays import vbo
import numpy as np
import os

class ModelTransform():
    def __init__(self):
        
        self.t3v1=np.array([0,0,0]).astype(float)
        self.t3v3rz=np.array([[0,0,0],[0,0,0],[0,0,1]]).astype(float)
        
    def model(self,vertices,faces):
        return np.require(vertices[faces].ravel(),np.float32,'F')
            
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
