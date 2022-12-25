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

with open("aoc2022/18.txt") as f:
    lines = [x.strip() for x in f]
    cubes = []
    for line in lines:
        x, y, z = [int(i) for i in line.split(',')]
        cubes.append((x,y,z))
        
    print(placeCubes(cubes))

    
    
    