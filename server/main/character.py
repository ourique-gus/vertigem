import numpy as np

class Character():
    def __init__(self,game, pid, x, y, theta):
        self.game=game
        self.pid=pid
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0
        self.theta=theta
        self.health=100
        self.controls=[0,0,0,0]
        self.vmod=5
        
    def update(self):
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
        
