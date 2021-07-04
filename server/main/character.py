import numpy as np
from main.projectile import Projectile

class Character():
    def __init__(self,server, pid, x, y, theta):
        self.server=server
        self.pid=pid
        self.kind='Character'
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0
        self.r=10
        self.theta=theta
        self.health=100
        self.controls=[0,0,0,0,0,0]
        self.vmod=5
        self.max_delay=10
        self.delay=0
        self.event='None'
        
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
        
        if self.controls[4] and not self.delay:
            self.delay=self.max_delay
            pid=np.random.randint(1,self.server.networking.max_id)
            while pid in self.server.networking.client_threads:
                pid=np.random.randint(1,self.server.networking.max_id)
            angle=self.controls[5]/1000.
            delta=20
            cangle=np.cos(angle)
            sangle=np.sin(angle)
            vm=np.sqrt(self.vx*self.vx+self.vy*self.vy)
            self.server.entities[pid]=Projectile(self.server, pid,self.x+np.cos(angle)*delta,self.y+np.sin(angle)*delta,2*vm*self.vmod*cangle,2*vm*self.vmod*sangle)
        
