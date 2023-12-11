import aoc
import re
import math
from collections import defaultdict
import numpy as np
from itertools import combinations

PART1_MUL = 2
PART2_MUL = 1000000

def loop(lines):
    # determine empty rows and cols
    double_x = set()
    double_y = set()
    galaxies = []
    for i, l in enumerate(lines):
        if np.all(l == '.'):
            double_y.add(i)
    for i, l in enumerate(lines.T):
        if np.all(l == '.'):
            double_x.add(i)
    
    #find galaxies
    w = np.where(lines == '#')
    for i in range(len(w[0])):
        galaxies.append((w[0][i], w[1][i])) 
    
    #sum distances
    sum = 0
    sum_empty = 0 
    for p1, p2 in combinations(galaxies,2):
        maxY = max(p1[0], p2[0])
        minY = min(p1[0], p2[0])
        maxX = max(p1[1], p2[1])
        minX = min(p1[1], p2[1])
        for y in range(minY,maxY):
            sum += 1
            if y in double_y: sum_empty += 1
        for x in range(minX,maxX):
            sum += 1
            if x in double_x: sum_empty += 1
    part1 = sum+sum_empty*(PART1_MUL-1)
    part2 = sum+sum_empty*(PART2_MUL-1)
    print('part 1:', part1)
    print('part 2:', part2)
        
    

lines = aoc.input_as_lines("input/11.txt")
lines = np.array(list(map(lambda l: [ *l], lines)))
loop(lines)