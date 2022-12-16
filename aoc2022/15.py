import re
import numpy as np
np.set_printoptions(linewidth=np.inf)

class Sensor:
    def __init__(self, input) -> None:
        self.sx = int(input[0])
        self.sy = int(input[1])
        self.bx = int(input[2])
        self.by = int(input[3])
        self.dist = calcDist(self.sx, self.sy, self.bx, self.by)
        
    def onSensor(self, x, y ):
        return self.sx == x and self.sy == y
    
    def onBeacon(self, x, y ):
        return self.bx == x and self.by == y
        
    def withinRange(self, x,y):
        if calcDist(self.sx, self.sy, x, y) <= self.dist:
            return True
        return False
    
    def beaconLess(self, x, y):
        if not self.onBeacon(x,y) and self.withinRange(x,y):
            return True
        return False
    
    def checkBorderPoints(self, lmin, lmax, sensors):
        dist = self.dist +1
        for i in range(0, dist+1):
            p = []
            if lmin <= (self.sx - dist + i) <= lmax and lmin <= self.sy - i <= lmax:
                p.append([self.sx - dist + i,self.sy - i])
            if lmin <= (self.sx - dist + i) <= lmax and lmin <= self.sy + i <= lmax:
                p.append([self.sx - dist + i,self.sy + i])
            if lmin <= (self.sx + dist + i) <= lmax and lmin <= self.sy + i <= lmax:
                p.append([self.sx + dist - i,self.sy + i])
            if lmin <= (self.sx + dist + i) <= lmax and lmin <= self.sy - i <= lmax:
                p.append([self.sx + dist - i,self.sy - i])
            for pp in p:
                isIn = False
                for s in sensors:
                    if not isIn and s!= self and s.withinRange(pp[0],pp[1]):
                        isIn = True
                if not isIn:
                    print('RESULT', pp)
                    print('RESULT', pp[0]*4000000 + pp[1])
                    return True        
        return False
    
    def __repr__(self) -> str:
        return '{('+str(self.sx)+','+str(self.sy)+'):'+ str(self.dist)+'}'

def calcDist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def analyzePoint(x,y, sensors):
    c = '.'
    for s in sensors:
        if s.onSensor(x, y):
            if (c in ['.', '#']): 
                c = 'S'
                break
            else: assert(False)
        elif s.onBeacon(x, y):
            if (c in ['.', '#']): 
                c = 'B'
                break
            else: assert(False)
        elif s.withinRange(x, y):
            if (c == '.'): 
                c = '#'
    return c

def analyzeSensors(sensors, bmin = 0, bmax = 20):
    pointsToCheck = []
    for s in sensors:
        if (s.checkBorderPoints(bmin, bmax, sensors)): 
            return
        print('sensor ', s)

def analyzeRow(row, sensors, minX, maxX):
    sum = 0
    strow = ''
    for xx in range(minX, maxX):
        c = '.'
        for s in sensors:
            if s.onSensor(xx, row):
                if (c in ['.', '#']): 
                    c = 'S'
                    break
                else: assert(False)
            elif s.onBeacon(xx, row):
                if (c in ['.', '#']): 
                    c = 'B'
                    break
                else: assert(False)
            elif s.withinRange(xx, row):
                if (c == '.'): 
                    c = '#'
        if c == '#':
            sum += 1
        strow += c
    
    print('PART 1: ', sum)
    # print(strow)

with open("aoc2022/15.txt") as f:
    lines = [x.strip() for x in f]
    input = np.zeros([len(lines), 4], dtype=int)
    sensors = []
    for line in lines:
        xs, ys, xb, yb = re.search(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups()
        sensors.append(Sensor([xs, ys, xb, yb]))    

    #part 1
    print('--- PART 1 ---')
    maxDist = max([a.dist for a in sensors])
    analyzeRow(2000000, sensors, -1031499-maxDist-5, 3994355+maxDist+5)
    #analyzeRow(10, sensors, -5, 27)
    
    #part 2
    print('--- PART 2 ---')
    #dim = 20
    dim = 4000000
    analyzeSensors(sensors, 0, dim)
    
    
    