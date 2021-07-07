from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

class Screen():
    def __init__(self, game, width, height):
        self.game=game
        self.width=width
        self.height=height
        
    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF | pygame.OPENGL)
        glClearColor(0.0, 0.0, 0.0, 1.0); 
        glEnable(GL_DEPTH_TEST)
        
    def update(self):
        glPushMatrix()
    
        self.game.camera.place_camera()
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
        
        glMatrixMode(GL_MODELVIEW);
        
        ent_zorder=[self.game.entities[ent].zorder if hasattr(self.game.entities[ent],"zorder") else -9999 for ent in self.game.entities]
        
        sorted_index=sorted(range(len(ent_zorder)), key=ent_zorder.__getitem__)
        keys=[ent for ent in self.game.entities]
        sorted_keys=[keys[index] for index in sorted_index]
        
        for ent in sorted_keys:
            if hasattr(self.game.entities[ent],"draw") \
               and (not hasattr(self.game.entities[ent],"is_hidden")  \
               or not self.game.entities[ent].is_hidden):
                self.game.entities[ent].draw()
                
                
        glPopMatrix()
        pygame.display.flip()
        
    def blit(self, *args):
        self.screen.blit(*args)
