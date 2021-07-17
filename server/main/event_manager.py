import pygame
import datetime
import time

class EventManager():
    def __init__(self,server, pid):
        self.server=server
        self.pid=pid
        self.kind='EventManager'
        
        self.max_duration=1/60.
        
        self.id_range=512
        self.events={}
        
    def register_event(self, etype, parameters):
        event_id=np.random.randint(0,self.id_range)
        if event_id in self.events:
            event_id=np.random.randint(0,self.id_range)
        
        self.events[event_id]={'time':stime, 'etype':etype,'parameters':parameters}
        
    def get_data(self, pid):
        event_string='/'.join([('{}|{}|'.format(event, self.events[event]['etype'])+'|'.join(['{}'.format(par) for par in self.events[event]['parameters']])) for event in self.events])
        return '10:['+event_string+']'
        
    def update(self):
        stime=time.time()
        keys=[key for key in self.events]
        for key in keys:
            if stime-self.events[key]['time'] > self.max_duration:
                self.events.pop(key)
        
