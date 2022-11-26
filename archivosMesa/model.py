import numpy as np
import mesa
import random
import matplotlib
import pandas as pd
from agent import CarAgent1
from agent import *
vec = []
class CarModel(mesa.Model):
    def __init__(self,N,width,height):
        global vec
        for i in range (5):
            vec.append(random.sample(range(0, 30), 2))
        self.numAgentsCar = N
        self.grid = mesa.space.MultiGrid(width,height,True)
        self.schedule = mesa.time.BaseScheduler(self)
        self.running = True
        for i in range(self.numAgentsCar):
            a = CarAgent1(i,self)
            self.schedule.add(a)
            x,y = vec[i]
            self.grid.place_agent(a,(x,y))
    def step(self):
        self.schedule.step()