# -- coding: utf-8 --

'''
Created on 14. 3. 2018

@author: JanRichter
'''

import math
import random
import timeit

class Point:
    def __init__(self, x: float, y: float, inCircle: bool):
        self.x = x 
        self.y = y 
        self.inCircle = inCircle
    
    def __str__(self):
        if (self.inCircle):
            return "Point ["+ str(self.x) + ";" + str(self.y) +"] is in circle"
        return "Point ["+ str(self.x) + ";" + str(self.y) +"] is NOT in circle"

    
class MonteCarloPi:
    def __init__(self, pointsAmount: int):
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
        if (math.sqrt(x**2 + y**2) < 1):
            return True
        return False
    
# --------------------------------------------------------------------------------------------------------------------------   
start = timeit.default_timer()
generator = MonteCarloPi(10000000)
stop = timeit.default_timer()
print("It took", round(stop - start, 4), "seconds to init the MonteCarloPi class.")

start = timeit.default_timer()
generator.generatePoints()
stop = timeit.default_timer()
print("It took", round(stop - start, 4), "seconds to generate", generator.pointsAmount , "points and evaluate if they're in the circle.")

start = timeit.default_timer()
print("Approximated pi value is", generator.approximatePi())
stop = timeit.default_timer()
print("It took", round(stop - start, 4), "seconds to approximate the value of Pi.")