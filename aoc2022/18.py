import re
import numpy as np
np.set_printoptions(linewidth=np.inf)

ADJACENT_VOXELS = [
    [-1,0,0],
    [1,0,0],
    [0,-1,0],
    [0,1,0],
    [0,0,-1],
    [0,0,1],
]

def placeCubes(cubes):
    cubesSet = set(cubes)
    walls = 0
    for c in cubes:
        for m in ADJACENT_VOXELS:
            if ((c[0]+m[0], c[1]+m[1], c[2]+m[2])) not in cubesSet:
                walls += 1
    return walls

def reachableCubes(cubes):
    MINV = 0
    MAXV = 22
    
    cubesSet = set(cubes)
    visited = set()
    walls = 0
    queue = [(0,0,0)]
    while (len(queue) > 0):
        c = queue.pop(0)
        for m in ADJACENT_VOXELS:
            adjacent = (c[0]+m[0], c[1]+m[1], c[2]+m[2])
            if adjacent in cubesSet:
                walls += 1
            elif adjacent not in visited and False not in [bool(MINV <= val <= MAXV) for val in adjacent]:
                #inbouds
                visited.add(adjacent)
                queue.append(adjacent)
    return walls  


with open("aoc2022/18.txt") as f:
    lines = [x.strip() for x in f]
    cubes = []
    for line in lines:
        x, y, z = [int(i) for i in line.split(',')]
        cubes.append((x,y,z))
        
    # print('part1')
    # print(placeCubes(cubes))
    
    print('part2')
    print(reachableCubes(cubes))

    
    
    