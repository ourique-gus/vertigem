import numpy as np
from main.projectile_spawner import ProjectileSpawner
from main.projectile import Projectile

class Character():
    def __init__(self,server, pid, x, y, angle):
        self.server=server
        self.pid=pid
        self.kind='Character'
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0
        self.r=10
        self.angle=angle
        self.health=100
        self.controls=[0,0,0,0,0,0]
        self.vmod=5
        self.max_delay=10
        self.delay=0
        self.event='None'
        self.proj_speed=5.1
        
    def look_for_collider(self):
        for ent in self.server.entities:
            if self.server.entities[ent].kind=='Collider':
                collision=self.server.entities[ent].get_collision(self.x,self.y,self.r)
                if collision:
                    self.x+=collision[0]
                    self.y+=collision[1]
                
    def collide(self):
        pass
        
    def update(self):
        self.angle=self.controls[5]/1000.
        cangle=np.cos(self.angle)
        sangle=np.sin(self.angle)
        if self.delay:
            self.delay-=1
        dvx=(-self.controls[1]+self.controls[3])
        dvy=(-self.controls[0]+self.controls[2])
        vx=-cangle*dvy+sangle*dvx
        vy=-sangle*dvy-cangle*dvx

        vr=np.sqrt(vx*vx+vy*vy)
        if vr > 0:
            self.vx=vx/vr*self.vmod
            self.vy=vy/vr*self.vmod
        else:
            vrr=np.sqrt(self.vx*self.vx+self.vy*self.vy)
            vr_var=vrr-self.vmod*0.05
            if vrr > 0 and vr_var > 0:
                self.vx=self.vx/vrr*vr_var
                self.vy=self.vy/vrr*vr_var
            else:
                self.vx=0
                self.vy=0
        self.x+=self.vx
        self.y+=self.vy
        
        self.look_for_collider()
        
        if self.controls[4] and not self.delay:
            self.delay=self.max_delay
            pid=np.random.randint(1,self.server.networking.max_id)
            while pid in self.server.networking.client_threads:
                pid=np.random.randint(1,self.server.networking.max_id)
            delta=20
            self.server.entities[pid]=Projectile(self.server, pid,self.x+cangle*delta,self.y+sangle*delta,self.proj_speed*cangle+self.vx,self.proj_speed*sangle+self.vy)



        
