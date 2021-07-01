import numpy as np
from main.projectile import Projectile

class Character():
    def __init__(self,server, pid, x, y, theta):
        self.server=server
        self.pid=pid
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0
        self.theta=theta
        self.health=100
        self.controls=[0,0,0,0]
        self.vmod=5
        self.max_delay=10
        self.delay=0
        
    def update(self):
        if self.delay:
            self.delay-=1
        vx=-self.controls[1]+self.controls[3]
        vy=-self.controls[0]+self.controls[2]
        vr=np.sqrt(vx*vx+vy*vy)
        if vr > 0:
            self.vx=vx/vr
            self.vy=vy/vr
        else:
            vrr=np.sqrt(self.vx*self.vx+self.vy*self.vy)
            vr_var=vrr-self.vmod*0.01
            if vrr > 0 and vr_var > 0:
                self.vx=self.vx/vrr*vr_var
                self.vy=self.vy/vrr*vr_var
            else:
                self.vx=0
                self.vy=0
        self.x+=self.vx*self.vmod
        self.y+=self.vy*self.vmod
        
        vr=np.sqrt(self.vx*self.vx+self.vy*self.vy)
        if vr and self.controls[4] and not self.delay:
            self.delay=self.max_delay
            pid=np.random.randint(1,self.server.networking.max_id)
            while pid in self.server.networking.client_threads:
                pid=np.random.randint(1,self.server.networking.max_id)
            self.server.entities[pid]=Projectile(self.server, pid,self.x,self.y,2*self.vx*self.vmod,2*self.vy*self.vmod)
        
