import aoc
import re
import math
from collections import defaultdict
import numpy as np
from itertools import combinations

def loop(lines):
    print(lines)
    double_x = set()
    double_y = set()
    galaxies = []
    for i, l in enumerate(lines):
        if np.all(l == '.'):
            double_y.add(i)
    for i, l in enumerate(lines.T):
        if np.all(l == '.'):
            double_x.add(i)
    # print(double_y, double_x)
    
    w = np.where(lines == '#')
    for i in range(len(w[0])):
        galaxies.append((w[0][i], w[1][i]))
    # print(galaxies)
    print(len(list(combinations(galaxies, 2))))
    
    sum = 0
    for p1, p2 in combinations(galaxies,2):
        maxY = max(p1[0], p2[0])
        minY = min(p1[0], p2[0])
        maxX = max(p1[1], p2[1])
        minX = min(p1[1], p2[1])
        countX = 0
        countY = 0
        for y in range(minY,maxY):
            countY += 1
            if y in double_y: countY+= 1
        for x in range(minX,maxX):
            countX += 1
            if x in double_x: countX+= 1
        count = countX + countY
        sum+=count
    print(sum)
        
    

lines = aoc.input_as_lines("input/11.txt")
lines = np.array(list(map(lambda l: [ *l], lines)))
#part 1
print('part 1:')
loop(lines)