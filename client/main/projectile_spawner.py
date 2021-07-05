import numpy as np
from main.projectile import Projectile

class ProjectileSpawner():
    def __init__(self,game, pid, x, y, vx, vy, theta):
        self.game=game
        self.pid=pid
        self.kind='ProjectileSpawner'
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.tick=0
        self.event='None'
        self.r=5
        
        pid=np.random.randint(self.game.max_server_pid+1,2*self.game.max_server_pid)
        while pid in self.game.entities:
            pid=np.random.randint(self.game.max_server_pid+1,2*self.game.max_server_pid)
        delta=20

        self.game.entities[pid]=Projectile(self.game, pid,self.x, self.y, self.vx, self.vy, theta)
        self.remove=True
