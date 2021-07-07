import numpy as np

class Projectile():
    def __init__(self,server, pid, x, y, vx, vy):
        self.server=server
        self.pid=pid
        self.kind='Projectile'
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.tick=0
        self.event='None'
        self.r=5
        
    def look_for_collider(self):
        for ent in self.server.entities:
            if self.server.entities[ent].kind=='Collider':
                collision=self.server.entities[ent].get_collision(self.x,self.y,self.r)
                if collision:
                    return True
        
    def update(self):
        self.tick+=1
        self.x+=self.vx
        self.y+=self.vy
        for pid in self.server.entities:
            if self.server.entities[pid].kind=='Character':
                dx=self.x-self.server.entities[pid].x
                dy=self.y-self.server.entities[pid].y
                drsq=dx*dx+dy*dy
                drvar=self.r+self.server.entities[pid].r
                if drsq < drvar*drvar:
                    self.server.entities[pid].x=(np.random.rand()-0.5)*450
                    self.server.entities[pid].y=(np.random.rand()-0.5)*450

        if self.look_for_collider():
            self.remove=True
        
        if self.tick > 300:
            self.remove=True
