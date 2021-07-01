import numpy as np

class Projectile():
    def __init__(self,game, pid, x, y, vx, vy):
        self.game=game
        self.pid=pid
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.tick=0
        
    def update(self):
        self.tick+=1
        self.x+=self.vx
        self.y+=self.vy
        if self.tick > 600:
            self.remove=True
