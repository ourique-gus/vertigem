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
                    self.server.entities[pid].x=np.random.rand()*1366
                    self.server.entities[pid].y=np.random.rand()*768
        
        if self.tick > 600:
            self.remove=True
