from OpenGL.arrays import vbo   
import numpy as np
import os

class ModelLoader():
    def __init__(self,game):
        self.game=game
        self.model_path_list={
            'ship':['models', 'ship.npz']
        }
        
        self.models={}
        
    def add_model_path(self, model_name,path_step):
        path=path_step.split('/')
        if len(path) == 1:
            path=path_step.split('\\')
        self.model_path_list[model_name]=path
        
    def load_model(self,model_name):
        path=os.path.join(*self.model_path_list[model_name])
        model=np.load(path)
        self.models[model_name]=model
        
    def load_all_models(self):
        for model in self.model_path_list:
            self.load_model(model)
            
