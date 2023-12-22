import numpy as np
from collections import defaultdict
from queue import PriorityQueue

def to_voxels(block):
    f,t = block
    voxels = set()
    for y in range(f[0],t[0]+1):
        for x in range(f[1],t[1]+1):
            for z in range(f[2],t[2]+1):
                voxels.add((y,x,z))
    return voxels

def check_level_down(world, voxels):
    res = set()
    for y,x,z in voxels:
        if z == 1:
            return (False, voxels)
        if (y,x,z-1) in world:
            return (False, voxels)
        res.add((y,x,z-1))
    return (True, res)
    
def part1(input):
    print(input)
    
    blocks = []
    world = set()
    maxz = 1
    #set up world
    for i in input:
        maxz = max(maxz, i[0][2], i[1][2])
        world.update(to_voxels(i))
        blocks.append(i)
    #move blocks down
    for curz in range(1,maxz+1):
        print(curz)
        for b in blocks:
            if b[0][2] == curz or b[1][2] == curz:
                #move down
                voxels = to_voxels(b)
                world.difference_update(voxels)
                while True:
                    success, voxels = check_level_down(world, voxels)
                    if success:
                        b[0][2] -= 1
                        b[1][2] -= 1
                    else:
                        world.update(voxels)
                        break
    #check blocks
    res = []
    for b in blocks:
        voxels = to_voxels(b)
        world.difference_update(voxels)
        important = False
        for bb in blocks:
            if bb != b:
                vs = to_voxels(bb)
                world.difference_update(vs)
                success, _ = check_level_down(world, vs)
                if success:
                    important = True
                    world.update(vs)
                    break
                world.update(vs)
        if not important:
            res.append(b)
        world.update(voxels)
                
    print('Part1', len(res))
    
    
    

with open("input/22.txt") as f:
    lines = f.read().rstrip().split('\n')
    input = [[ list(map(int,c1.split(','))), list(map(int,c2.split(',')))]for c1,c2 in (l.split('~') for l in lines)]
    part1(input)