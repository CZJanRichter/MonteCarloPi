# -- coding: utf-8 --

'''
Created on 14. 3. 2018

@author: JanRichter
'''

from __future__ import division
import math
import random
import timeit


class Point:
    '''
    x: float
    y: float
    inCircle: bool
    '''
    def __init__(self, x, y, inCircle):
        self.x = x 
        self.y = y 
        self.inCircle = inCircle
    
    def __str__(self):
        if (self.inCircle):
            return "Point ["+ str(self.x) + ";" + str(self.y) +"] is in circle"
        return "Point ["+ str(self.x) + ";" + str(self.y) +"] is NOT in circle"

    
class MonteCarloPi:
    '''
    pointsAmount: int
    '''
    def __init__(self, pointsAmount):
        self.pointsAmount = pointsAmount
        self.pointsInCircle = []
        self.pointsOutsideOfCircle = []
    
    def approximatePi(self):
        return 4 * (len(self.pointsInCircle) / self.pointsAmount)
        
    def generatePoints(self):
        for _ in range(0, self.pointsAmount):
            x = random.uniform(0,1)
            y = random.uniform(0,1)
            inCircle = self.isPointInsideCircle(x, y)
            if (inCircle):
                self.pointsInCircle.append(Point(x, y, inCircle))
            else:
                self.pointsOutsideOfCircle.append(Point(x, y, inCircle))
            
    def isPointInsideCircle(self, x, y):
        '''
        x: float
        y: float
        '''
        if (math.sqrt(x**2 + y**2) < 1):
            return True
        return False
    
# --------------------------------------------------------------------------------------------------------------------------   
start = timeit.default_timer()
generator = MonteCarloPi(1000000)
stop = timeit.default_timer()
print "It took", ; print round(stop - start, 4), ; print "seconds to init the MonteCarloPi class."

start = timeit.default_timer()
generator.generatePoints()
stop = timeit.default_timer()
print "It took", ; print round(stop - start, 4), ; print "seconds to generate", ; print generator.pointsAmount, ; print "points and evaluate if they're in the circle."

start = timeit.default_timer()
print "Approximated pi value is", ; print generator.approximatePi()
stop = timeit.default_timer()
print "It took", ; print round(stop - start, 4), ; print "seconds to approximate the value of Pi."
