import pygame
import numpy as np
from main import fx

def FXProjectileHit(game,par):
    x=float(par[0])/1000
    y=float(par[1])/1000
    
    num=10
    for i in range(num):
        vel=(np.random.rand(3)-0.5)
        game.entity_manager.spawn_entity(fx.RandomCube, x, y, vel[0], vel[1], vel[2])
        
def FXProjectileHitCharacter(game,par):
    x=float(par[0])/1000
    y=float(par[1])/1000
    
    num=10
    for i in range(num):
        vel=(np.random.rand(3)-0.5)
        game.entity_manager.spawn_entity(fx.RedCube, x, y, vel[0], vel[1], vel[2])
        
def DestroyCharacter(game,par):
    x=float(par[0])/1000
    y=float(par[1])/1000
    
    num=30
    for i in range(num):
        vel=(np.random.rand(3)-0.5)
        game.entity_manager.spawn_entity(fx.RedCube, x, y, vel[0], vel[1], vel[2])
        
def HideCharacter(game,par):
    game.entity_manager.entities[int(par[0])].is_hidden=True


def ShowCharacter(game,par):
    game.entity_manager.entities[int(par[0])].is_hidden=False
