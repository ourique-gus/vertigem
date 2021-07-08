from OpenGL.arrays import vbo   
import numpy as np
import pygame
import os

class ModelLoader():
    def __init__(self,game):
        self.game=game
        self.model_path_list={
            'ship':{'model':['models', 'ship.npz'], 'texture':['models', 'ship.png'] },
            'cube':{'model':['models', 'cube.npz'], 'texture':['models', 'cube.png'] },
        }
        
        self.models={}
        
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
        
    def load_all_models(self):
        for model in self.model_path_list:
            self.load_model(model)
            
