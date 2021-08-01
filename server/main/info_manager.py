import numpy as np

class InfoManager():
    def __init__(self,server, pid):
        self.server=server
        self.pid=pid
        self.info={}
        self.kind='InfoManager'
        
        self.itype_fromto={
            'ping':0,
            'player_data':1,
        }
        
    def get_data(self, pid):
        
        info_string='/'.join([
            '{}|'.format(self.itype_fromto[info])+'|'.join(['{}'.format(par) for par in self.info[pid][info]])
            for info in self.info[pid] if info in self.itype_fromto])
        
        return '0:[' + info_string +']'


    def update(self):
        for pid in self.server.entity_manager.entities:
            if self.server.entity_manager.entities[pid].kind=='Character':
                self.info[pid]['ping']=[0]
                self.info[pid]['player_data']=[int(self.server.entity_manager.entities[pid].health)]
