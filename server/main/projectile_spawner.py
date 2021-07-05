import numpy as np
from main.projectile import Projectile

class ProjectileSpawner():
    def __init__(self,server, pid, x, y, vx, vy):
        self.server=server
        self.pid=pid
        self.kind='ProjectileSpawner'
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.tick=0
        self.event='None'
        self.r=5
        
        pid=np.random.randint(self.server.networking.max_id+1,2*self.server.networking.max_id)
        while pid in self.server.entities:
            pid=np.random.randint(self.server.networking.max_id+1,2*self.server.networking.max_id)
        delta=20

        self.server.entities[pid]=Projectile(self.server, pid,self.x, self.y, self.vx, self.vy)
        self.remove=True
