import numpy as np

class Collider():
    def __init__(self,server, pid, xi, yi, xf, yf):
        self.server=server
        self.pid=pid
        self.kind='Collider'
        self.xi=xi
        self.yi=yi
        self.xf=xf
        self.yf=yf
        
    def update(self):
        pass
        
