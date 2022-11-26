import numpy as np
import mesa
import random
import matplotlib
import pandas as pd
from model import *

speedGlobal = []

class CarAgent1(mesa.Agent):
    global speedGlobal
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id

    def move(self):
        x,y = self.pos
        self.newPos = (x+1,y)
        self.speed = [self.newPos[0]-self.pos[0], self.newPos[1]-self.pos[1]]
        speedGlobal = self.speed
        self.model.grid.move_agent(self,(x + 1, y))
    
    def step(self):
        self.move()
        print(self.speed)