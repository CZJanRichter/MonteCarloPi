# -- coding: utf-8 --

'''
Created on 15. 5. 2018

@author: JanRichter
'''

from __future__ import division
import math
import multiprocessing
import random
import threading
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
        self.pointsPerThread = pointsAmount
        self.pointsInCircle = []
        self.pointsOutsideOfCircle = []
        self.threads = []
    
    def approximatePi(self):
        print "Amount of points in circle:", ; print len(self.pointsInCircle)
        print "Amount of points outside of circle:", ; print len(self.pointsOutsideOfCircle)
        print "Amount of points:", ; print len(self.pointsInCircle)+len(self.pointsOutsideOfCircle)
        return 4 * (len(self.pointsInCircle) / self.pointsAmount)

    def generatePoints(self):
        for _ in range(0, self.pointsPerThread):
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

    def runThreadsToGeneratePoints(self, threadAmount):
        '''
        threadAmount: int
        '''
        self.pointsPerThread = int(self.pointsAmount / threadAmount)
        for _ in range(0, threadAmount):
            newThread = threading.Thread(target=self.generatePoints)
            self.threads.append(newThread)
        for thread in self.threads:
            thread.start()
        print "Created thread amount:", ; print len(self.threads)
        print "Active Python thread amount:", ; print threading.active_count()
        for thread in self.threads:
            thread.join()
        if ((len(self.pointsInCircle)+len(self.pointsOutsideOfCircle)) < self.pointsAmount):
            self.pointsPerThread = self.pointsAmount-len(self.pointsInCircle)-len(self.pointsOutsideOfCircle)
            self.generatePoints()
    
# --------------------------------------------------------------------------------------------------------------------------   
start = timeit.default_timer()
generator = MonteCarloPi(1000000)
stop = timeit.default_timer()
print "It took", ; print round(stop - start, 4), ; print "seconds to init the MonteCarloPi class."

start = timeit.default_timer()
generator.runThreadsToGeneratePoints(multiprocessing.cpu_count())
stop = timeit.default_timer()
print "It took", ; print round(stop - start, 4), ; print "seconds to generate", ; print generator.pointsAmount, ; print "points and evaluate if they're in the circle."

start = timeit.default_timer()
print "Approximated pi value is", ; print generator.approximatePi()
stop = timeit.default_timer()
print "It took", ; print round(stop - start, 4), ; print "seconds to approximate the value of Pi."

