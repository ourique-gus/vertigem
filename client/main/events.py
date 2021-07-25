import pygame
import numpy as np
from main.fx import RandomCube

def FXProjectileHit(game,par):
    x=float(par[0])/1000
    y=float(par[1])/1000
    
    num=10
    for i in range(num):
        vel=(np.random.rand(3)-0.5)
        game.entity_manager.spawn_entity(RandomCube, x, y, vel[0], vel[1], vel[2])
