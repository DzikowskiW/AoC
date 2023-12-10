import aoc
import re
from copy import deepcopy
import math
from collections import defaultdict
import numpy as np
import sys
from PIL import Image
np.set_printoptions(threshold=sys.maxsize)

mapp = {
    '|': [(-1,0), (1,0)],
    '-': [(0,-1), (0,1)],
    'L' : [(-1,0), (0,1)],
    'J' : [(0,-1), (-1,0)],
    '7' : [(1,0), (0,-1)],
    'F' : [(1,0), (0,1)],
    '.' : [],
}

scale_map = {
    '|':  [(0,1), (1,1), (2,1)],
    '-':  [(1,0), (1,1), (1,2)],
    'L' : [(0,1), (1,1), (1,2)],
    'J' : [(0,1), (1,1), (1,0)],
    '7' : [(1,0), (1,1), (2,1)],
    'F' : [(1,2), (1,1), (2,1)],
    '.' : [],
}

def find_start_coords(lines):
    for y,l in enumerate(lines): 
        x  = l.rfind('S')
        if x  > -1:
            return (y,x)
        
def find_start_steps(lines, start):
    nextSteps = []
    shape = []
    for nxt in [(-1,0), (1, 0), (0, 1), (0, -1)]:
        point = (start[0] + nxt[0], start[1] + nxt[1])
        if (-nxt[0], -nxt[1]) in mapp[lines[point[0]][point[1]]]:
            shape.append((nxt[0], nxt[1]))
            nextSteps.append(point)
    # print('shape', shape[0])
    v = '.'
    for k in scale_map.keys():
        if shape[0] in mapp[k] and shape[1] in mapp[k]:
            v = k
            break
    # print('start type', v)
    return (v, nextSteps[0], nextSteps[1]);
    
def find_next_step(lines, prev, path):
    for nxt in mapp[lines[path[0]][path[1]]]:
        point = (path[0] + nxt[0], path[1] + nxt[1])
        if point != prev:
            return point


def loop(lines):
    #find Start
    start = find_start_coords(lines)
    start_letter, path1, path2 = find_start_steps(lines, start)
    path1_prev = start
    path2_prev = start
    dist = 1
    path_points = set()
    path_points.add(start)
    path_points.add(path1)
    path_points.add(path2)
    while path1 != path2:
        p1 = find_next_step(lines, path1_prev, path1)
        path1_prev = path1
        path1 = p1
        p2 = find_next_step(lines, path2_prev, path2)
        path2_prev = path2
        path2 = p2
        dist +=1
        path_points.add(path1)
        path_points.add(path2)    
    print('part1', dist)
    
    scale_map['S'] = scale_map[start_letter]
    arr = np.zeros((len(lines)*3, len(lines[0])*3), dtype=int)
    # print(path_points)
    for p in path_points:
        y = p[0]*3
        x = p[1]*3
        n = lines[p[0]][p[1]]
        for dy, dx in scale_map[n]:
            arr[y+dy][x+dx] = 1
    # print(arr)    
    
    np.savetxt('test.txt', arr, fmt='%d')

    #mark inside points
    start_inside = {
            'L' : (0,2),
            'J' : (0,0),
            '7' : (2,0),
            'F' : (2,2)
    }
    insidePoints = set()
    insidePoints.add((
        start[0]*3+start_inside[start_letter][0],
        start[1]*3+start_inside[start_letter][1],
        ))
    # print(start_letter, start, insidePoints)
    while (len(insidePoints) > 0):
        p = insidePoints.pop()
        arr[p] = 2
        for i in range(p[0]-1, min(p[0]+2, len(arr))):
            for j in range(p[1]-1, min(p[1]+2, len(arr[0]))):
                if arr[i,j] == 0:
                    insidePoints.add((i,j))
    # print(arr)    
    np.savetxt('test.txt', arr, fmt='%d')
    #find tiles
    tiles = 0
    tiles_zero = 0
    for i in range(0,len(arr),3):
        for j in range(0, len(arr[0]),3):
            tile = True
            tile_zero = True
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if arr[k,l] != 2:
                        tile = False
                    if arr[k,l] != 0:
                        tile_zero = False
            if tile:
                tiles +=1
            if tile_zero:
                tiles_zero += 1
    print(tiles, tiles_zero)
    
lines = aoc.input_as_lines("input/10.txt")
loop(lines)
#5561 493