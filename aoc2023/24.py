import numpy as np
from collections import defaultdict
from heapq import heappop, heappush
import functools
from copy import deepcopy
from itertools import combinations


# LIMITS = (7,27) 
LIMITS = (200000000000000, 400000000000000) 

def part1(paths, limits = LIMITS):
    checked = set()
    count = 0
    for p1, p2 in combinations(paths, 2):    
            if p1 != p2:
                checked.add((str(p1),str(p2)))
                x1, y1, _ = p1[0]
                dx1, dy1, _ = p1[1] 
                x2,y2 = x1 + dx1, y1 + dy1
                x3, y3, _ = p2[0]
                dx3, dy3, _ = p2[1]
                x4, y4 = x3 + dx3, y3 + dy3
                denom = ((x1-x2)*(y3-y4) -  (y1-y2)*(x3-x4))
                if denom != 0:
                    px = ((x1*y2 - y1*x2)*(x3-x4)-(x1-x2)*(x3*y4 - y3*x4)) / denom
                    py = ((x1*y2 - y1*x2)*(y3-y4)-(y1-y2)*(x3*y4 - y3*x4)) / denom
                    if limits[0] <= px <= limits[1] and limits[0] <= py <= limits[1]:
                        #check if in future
                        if ((dx1 <= 0 and px <= x1) or (dx1 >= 0 and px >= x1)) and ((dy1 <= 0 and py <= y1) or (dy1 >= 0 and py >= y1)):
                            if ((dx3 <= 0 and px <= x3) or (dx3 >= 0 and px >= x3)) and ((dy3 <= 0 and py <= y3) or (dy3 >= 0 and py >= y3)):
                                # print(x1,y1, dx1, dy1,'|', x3,y3, 'res:', px, py)
                                count += 1
    print('Part1:', count)
            

with open("input/24.txt") as f:
    lines = f.read().rstrip().split('\n')
    paths = [(tuple(map(int,ll[0].split(', '))), tuple(map(int,ll[1].split(', ')))) for ll in (l.split(' @ ') for l in lines)]
    part1(paths)