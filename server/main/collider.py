import numpy as np

class Collider():
    def __init__(self,server, pid, xi, xf, yi, yf):
        self.server=server
        self.pid=pid
        self.kind='Collider'
        self.xi=xi
        self.yi=yi
        self.xf=xf
        self.yf=yf
        
    def get_collision(self, x, y, r):
        xl=-(x+r)+(self.xi)
        xr=+(x-r)-(self.xf)
        yt=(y-r)-(self.yf)
        yb=-(y+r)+(self.yi)
        dx=max([xl,xr])
        dy=max([yt,yb])
        if dx < 0 and dy < 0:
            if dx > dy:
                sign=xl > xr and -1 or 1
                return (-dx*sign, 0)
            else:
                sign=yt > yb and -1 or 1
                return (0,dy*sign)
        
    def update(self):
        pass
        
