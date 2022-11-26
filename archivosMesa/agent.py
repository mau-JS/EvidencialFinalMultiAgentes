import numpy as np
import mesa
import random
import pandas as pd

global posi
vec = []

class CarAgent1(mesa.Agent):
    def __init__(self,unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id

    def step(self):
        print(self.pos)