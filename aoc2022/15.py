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
        # if c in ['S', 'B']:
        #     break
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
    #print(checked)


def analyzeSensors1(sensors, bmin = 0, bmax = 20):
    pointsToCheck = []
    for s in sensors:
        dist = s.dist+1
        pointsToCheck += [[s.sx - dist, s.sy], [s.sx+dist, s.sy], [s.sx, s.sy-dist], [s.sx, s.sy+dist]]
    for p in pointsToCheck:
        if bmin <= p[0] <= bmax and bmin <= p[1] <= bmax:
            if analyzePoint(p[0],p[1],sensors) == '.':
                print(p)
                return

def analyzeRow(row, sensors, minX, maxX):
    sum = 0
    strow = ''
    cx = None
    for xx in range(minX, maxX):
        c = analyzePoint(xx, row, sensors)
        if c == '#':
            sum += 1
        elif c == '.':
            cx = xx
        strow += c
        
    #print(sum)
    print(strow)
    return cx  

with open("aoc2022/15.txt") as f:
    lines = [x.strip() for x in f]
    input = np.zeros([len(lines), 4], dtype=int)
    sensors = []
    i=0
    maxY = -1000
    minY = 1000
    
    maxX = -1000
    minX = 1000
    for line in lines:
        xs, ys, xb, yb = re.search(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups()
        sensors.append(Sensor([xs, ys, xb, yb]))
        if minY > int(ys): minY = int(ys)
        if minY > int(yb): minY = int(yb)
        if maxY < int(yb): maxY = int(yb)
        if maxY < int(ys): maxY = int(ys)
        if minX > int(xb): minX = int(xb)
        if minX > int(xs): minX = int(xs)
        if maxX < int(xb): maxX = int(xb)
        if maxX < int(xs): maxX = int(xs)
        i+=1
    
    # print(minX, maxX)
    # maxDist = max([a.dist for a in sensors])
    # print(maxDist)
    
    #dim = 20
    dim = 4000000
    
    # point = None
    # for y in range(0, dim+1):
    #     xx = analyzeRow(y, sensors, 0, dim+1)
    #     if xx is not None:
    #         point = [xx, y]
    # print(point[0], point[1])
    analyzeSensors(sensors, 0, dim)
    #analyzeRow(2000000, sensors, -1031499-maxDist-5, 3994355+maxDist+5)
    
    
    