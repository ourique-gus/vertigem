import pygame
import datetime
import time
from main.character import Character
from main.events import FXProjectileHit

class EventManager():
    def __init__(self,game, pid):
        self.kind='EventManager'
        self.game=game
        self.pid=pid
        
        self.max_duration=1/6.
        
        self.etype_fromto={
            1:FXProjectileHit,
        }
        
        self.events={}
        
    def run_event(self, etype, parameters):
        event_id=np.random.randint(0,self.id_range)
        if event_id in self.events:
            event_id=np.random.randint(0,self.id_range)
        
        self.events[event_id]={'time':stime, 'etype':etype,'parameters':parameters}
        
    def register_event(self, event_id):
        pass
        
    def set_data(self, data):
        stime=time.time()
        event_data=data.split('[')[-1].split(']')[0]
        events=event_data.split('/')
        for event in events:
            if event:
                event_var=event.split('|')
                event_id=int(event_var[0])
                event_type=int(event_var[1])
                event_par=event_var[2:]
                if not event_id in self.events:
                    self.events[event_id]=stime
                    self.etype_fromto[event_type](self.game,event_par)
                    
        pass
        
    def update(self):
        stime=time.time()
        keys=[key for key in self.events]
        for key in keys:
            if stime-self.events[key] > self.max_duration:
                self.events.pop(key)
        
