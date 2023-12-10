import aoc
import numpy as np

FLOOD_VAL = 2
SYMBOL_TO_XY_MAP = {
    '|': [(-1,0), (1,0)],
    '-': [(0,-1), (0,1)],
    'L' : [(-1,0), (0,1)],
    'J' : [(0,-1), (-1,0)],
    '7' : [(1,0), (0,-1)],
    'F' : [(1,0), (0,1)],
    '.' : [],
}

SCALE_MAP = {
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
        if (-nxt[0], -nxt[1]) in SYMBOL_TO_XY_MAP[lines[point[0]][point[1]]]:
            shape.append((nxt[0], nxt[1]))
            nextSteps.append(point)
    
    # figure out start shape
    v = '.'
    for k in SCALE_MAP.keys():
        if shape[0] in SYMBOL_TO_XY_MAP[k] and shape[1] in SYMBOL_TO_XY_MAP[k]:
            v = k
            break

    return (v, *nextSteps);
    
def find_next_step(lines, prev, path):
    for nxt in SYMBOL_TO_XY_MAP[lines[path[0]][path[1]]]:
        point = (path[0] + nxt[0], path[1] + nxt[1])
        if point != prev:
            return point

def loop(lines):
    # PART 1
    start = find_start_coords(lines)
    start_letter, *path = find_start_steps(lines, start)
    prev = [start , start]
    dist = 1
    path_points = set([start, *path])
    while path[0] != path[1]:
        p0 = find_next_step(lines, prev[0], path[0])
        p1 = find_next_step(lines, prev[1], path[1])
        prev = path
        path = [p0, p1]
        dist +=1
        for p in path: 
            path_points.add(p)
    print('part 1', dist)
    
    # PART 2
    # One char from lines = 3x3 matrix to include spaces between pipes
    #  e.g. J = 
    #  0 1 0
    #  1 1 0
    #  0 0 0
    SCALE_MAP['S'] = SCALE_MAP[start_letter]
    arr = np.zeros((len(lines)*3, len(lines[0])*3), dtype=int)
    for p in path_points:
        y = p[0]*3
        x = p[1]*3
        n = lines[p[0]][p[1]]
        for dy, dx in SCALE_MAP[n]:
            arr[y+dy][x+dx] = 1

    # flood
    pointsToFlood = set([(0,0)])
    while (len(pointsToFlood) > 0):
        p = pointsToFlood.pop()
        arr[p] = FLOOD_VAL
        for i in range(p[0]-1, min(p[0]+2, len(arr))):
            for j in range(p[1]-1, min(p[1]+2, len(arr[0]))):
                if arr[i,j] == 0:
                    pointsToFlood.add((i,j))
    
    # debug
    # np.savetxt('tmp.txt', arr, fmt='%d')
    
    #find tiles (3x3 of inside value)
    tiles_count = 0
    for i in range(0,len(arr),3):
        for j in range(0, len(arr[0]),3):
            if np.all(arr[i:i+3, j:j+3] == 0):
                tiles_count +=1
    print('part 2:', tiles_count)
    
lines = aoc.input_as_lines("input/10.txt")
loop(lines)