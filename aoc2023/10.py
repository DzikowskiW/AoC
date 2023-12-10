import aoc
import re
from copy import deepcopy
import math
from collections import defaultdict
import numpy as np

mapp = {
    '|': [(-1,0), (1,0)],
    '-': [(0,-1), (0,1)],
    'L' : [(-1,0), (0,1)],
    'J' : [(0,-1), (-1,0)],
    '7' : [(1,0), (0,-1)],
    'F' : [(1,0), (0,1)],
    '.' : [],
}

def find_start_coords(lines):
    for y,l in enumerate(lines): 
        x  = l.rfind('S')
        if x  > -1:
            return (y,x)
        
def find_start_steps(lines, start):
    nextSteps = []
    for nxt in [(-1,0), (1, 0), (0, 1), (0, -1)]:
        point = (start[0] + nxt[0], start[1] + nxt[1])
        if (-nxt[0], -nxt[1]) in mapp[lines[point[0]][point[1]]]:
            nextSteps.append(point)
    print(nextSteps)
    return nextSteps;
    
def find_next_step(lines, prev, path):
    print(lines[path[0]][path[1]])
    for nxt in mapp[lines[path[0]][path[1]]]:
        point = (path[0] + nxt[0], path[1] + nxt[1])
        if point != prev:
            return point

def loop(lines):
    #find Start
    start = find_start_coords(lines)
    path1, path2 = find_start_steps(lines, start)
    path1_prev = start
    path2_prev = start
    dist = 1
    while path1 != path2:
        p1 = find_next_step(lines, path1_prev, path1)
        path1_prev = path1
        path1 = p1
        p2 = find_next_step(lines, path2_prev, path2)
        path2_prev = path2
        path2 = p2
        dist +=1
        
    print(start, path1, path2)
    print('part1', dist)
        
    
    #loop from both
    
lines = aoc.input_as_lines("input/10.txt")
loop(lines)