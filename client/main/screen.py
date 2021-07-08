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
        glShadeModel(GL_SMOOTH)  
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE,  GL_MODULATE);
        
    def update(self):
        glPushMatrix()
    
        self.game.camera.place_camera()
        
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
        
        glMatrixMode(GL_MODELVIEW);
        
        glEnable(GL_LIGHT0)
        
        glLightfv(GL_LIGHT0, GL_POSITION, (50,50,100,1))
        #glLightfv(GL_LIGHT0, GL_AMBIENT, (0,0,1,1))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1,1,1,1))
        #glLightfv(GL_LIGHT0, GL_SPECULAR, (0,0,0,1))
        #glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, self.dir)
        #glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, self.exp)
        #glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, self.cut)
        #glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, self.att['CONSTANT'])
        #glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, self.att['LINEAR'])
        #glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, self.att['QUADRATIC'])
        
        
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
