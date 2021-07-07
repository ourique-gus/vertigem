from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

class Projectile():
    def __init__(self,game, pid, x, y, vx, vy, theta):
        self.game=game
        self.pid=pid
        self.kind='Projectile'
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.theta=theta
        self.r=5
        self.colour=(255,0,0,255)
        self.sprite=pygame.Surface((2*self.r, 2*self.r), flags=pygame.SRCALPHA)
        self.sprite.fill((255,255,255,0))
        pygame.draw.circle(self.sprite,self.colour,(self.r,self.r),self.r)
        self.sprite_size=self.sprite.get_size()
        self.tick=0
        
    def look_for_collider(self):
        for ent in self.game.entities:
            if self.game.entities[ent].kind=='Collider':
                collision=self.game.entities[ent].get_collision(self.x,self.y,self.r)
                if collision:
                    return True
        
    def update(self):
        self.tick+=1
        self.x+=self.vx
        self.y+=self.vy
        
        if self.tick > 300:
            self.remove=True
            
        if self.look_for_collider():
            self.remove=True
        
        
    def draw(self):
        #self.x+=self.vx
        #self.y+=self.vy
        #dx=self.x-self.game.camera.x
        #dy=self.y-self.game.camera.y
        #self.game.screen.blit(self.sprite, (
        #    dx*self.game.camera.cangle+dy*self.game.camera.sangle+self.game.screen.width/2-self.sprite_size[0]/2+self.game.camera.x_shift,
        #    -dx*self.game.camera.sangle+dy*self.game.camera.cangle+self.game.screen.height/2-self.sprite_size[1]/2+self.game.camera.y_shift
        #    )
        #)
        glBegin(GL_QUADS)
        glVertex3fv((self.x-2,self.y-2,0))
        glVertex3fv((self.x-2,self.y+2,0))
        glVertex3fv((self.x+2,self.y+2,0))
        glVertex3fv((self.x+2,self.y-2,0))
        glEnd()
        
    def set_pid(self,pid):
        self.pid=pid
