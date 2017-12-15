#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:43:53 2017

@author: wotsit2000
"""

import random

class Agent():
    def __init__(self, environment, agents, y = None, x = None):
        self._x = 0
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
        self._y = 0
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y
        self.environment = environment
        self.agents = agents
        self.store = 0
        
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value

    def dely(self):
        del self._y

    x = property(getx, setx, delx, "I'm the 'x' property")  
    y = property(gety, sety, dely, "I'm the 'y' property")              
    
    def __str__(self):
     return str(self._x) + " " + str(self._y)
 
    def eat(self): # can you make it eat what is left?
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
         
    def distance_between(self, agents):
        return (((self._x - agents._x)**2) + ((self._y - agents._y)**2))**0.5
        
    def share_with_neighbours(self, neighbourhood):
        for agents in self.agents:
            distance = self.distance_between(agents)
            if distance <= neighbourhood:
                sum = self.store + agents.store
                average = sum /2
                self.store = average
                agents.store = average
                #To check this works - print("sharing" + str(distance) + " " + str(average))