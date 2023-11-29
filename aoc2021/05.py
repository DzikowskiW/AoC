from functools import reduce
import operator
import re
import numpy as np
from collections import defaultdict

def p1(maxX, maxY, startCoords, endCoords):
    arr = np.zeros([maxY+1,maxX+1])
    #enter data
    for i in range(len(startCoords)):
        sc = startCoords[i]
        ec = endCoords[i]
        if (sc[0] == ec[0]):
            for j in range(min(sc[1], ec[1]), max(sc[1], ec[1])+1):
                arr[j, sc[0]] += 1
        elif  (sc[1] == ec[1]):
            for j in range(min(sc[0], ec[0]), max(sc[0], ec[0])+1):
                arr[sc[1], j] += 1
        # print(sc, '->', ec)
    sum = 0
    for a in arr:
        for v in a:
            if (v > 1): sum += 1
    print(sum)

def p2(maxX, maxY, startCoords, endCoords):
    arr = np.zeros([maxY+1,maxX+1])
    #enter data
    for i in range(len(startCoords)):
        sc = startCoords[i]
        ec = endCoords[i]
        if (sc[0] == ec[0]):
            for j in range(min(sc[1], ec[1]), max(sc[1], ec[1])+1):
                arr[j, sc[0]] += 1
        elif  (sc[1] == ec[1]):
            for j in range(min(sc[0], ec[0]), max(sc[0], ec[0])+1):
                arr[sc[1], j] += 1
        else: 
            xsign = 1 if sc[1] < ec[1] else -1
            ysign = 1 if sc[0] < ec[0] else -1
            xs = range(sc[1], ec[1]+xsign, xsign)
            ys = range(sc[0], ec[0]+ysign, ysign)
            for i in range(len(xs)):
                arr[xs[i], ys[i]] += 1
    sum = 0
    for a in arr:
        for v in a:
            if (v > 1): sum += 1
    # print(arr)
    print(sum)

with open("05.txt") as f:
    lines = [x.strip() for x in f]
    pattern = '^(\d+),(\d+) -> (\d+),(\d+)$'
    startCoords = []
    endCoords = []

    for line in lines:
        #input
        m = re.match(pattern, line)
        startCoords.append((int(m[1]), int(m[2])))
        endCoords.append((int(m[3]), int(m[4])))

    #get max dimensions
    maxX = max(reduce(lambda m,val : val[0] if val[0] > m else m, startCoords, 0), reduce(lambda m,val : val[0] if val[0] > m else m, endCoords, 0))
    maxY = max(reduce(lambda m,val : val[1] if val[1] > m else m, startCoords, 0), reduce(lambda m,val : val[1] if val[1] > m else m, endCoords, 0))
    
    # p1(maxX, maxY, startCoords, endCoords)
    p2(maxX, maxY, startCoords, endCoords)

    

    
