import pygame
import datetime
import time
import numpy as np

class EventManager():
    def __init__(self,server, pid):
        self.server=server
        self.pid=pid
        self.kind='EventManager'
        
        self.max_duration=1/6.
        
        self.etype_fromto={
            'fx_projectile_hit':1,
        }
        
        self.id_range=512
        self.events={}
        
    def register_event(self, etype, parameters):
        event_id=np.random.randint(0,self.id_range)
        if event_id in self.events:
            event_id=np.random.randint(0,self.id_range)
        
        self.events[event_id]={'time':time.time(), 'etype':self.etype_fromto[etype],'parameters':parameters}
        
    def get_data(self, pid):
        event_string='/'.join([('{}|{}|'.format(event, self.events[event]['etype'])+'|'.join(['{}'.format(par) for par in self.events[event]['parameters']])) for event in self.events])
        return '1:['+event_string+']'
        
    def update(self):
        stime=time.time()
        keys=[key for key in self.events]
        for key in keys:
            if stime-self.events[key]['time'] > self.max_duration:
                self.events.pop(key)
        
