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
    
    def __repr__(self) -> str:
        return '{('+str(self.sx)+','+str(self.sy)+'):'+ str(self.dist)+'}'

def calcDist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def plotSensor(cave, s, offsetX, offsetY):
    #calculate distanse to beacon
    dist = calcDist(*s)
    for xx in range(0, len(cave)):
        for yy in range(0, len(cave[0])):
            if (calcDist(s[0]+ offsetX, s[1] + offsetY, xx , yy)) <= dist:
                cave[xx, yy] = '1'
    return     

def analyzeRow(row, sensors, minX, maxX):
    sum = 0
    strow = ''
    for xx in range(minX, maxX):
        c = '.'
        for s in sensors:
            # if c in ['S', 'B']:
            #     break
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
    
    print(sum)
    #print(strow)

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
    
    print(minX, maxX)
    maxDist = max([a.dist for a in sensors])
    print(maxDist)
    # for y in range(-10,30):
    #     analyzeRow(y, sensors, -10, 35)
    analyzeRow(2000000, sensors, -1031499-maxDist-5, 3994355+maxDist+5)
    
    
    