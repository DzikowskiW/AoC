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
    blocks = []
    block_voxels = defaultdict(list)
    world = set()
    maxz = 1
    #set up world
    for i, inp in enumerate(input):
        maxz = max(maxz, inp[0][2], inp[1][2])
        block_voxels[i] = to_voxels(inp)
        world.update(block_voxels[i])
        blocks.append(inp)
    
    #move blocks down
    for curz in range(1,maxz+1):
        # print(curz)
        for i, b in enumerate(blocks):
            if b[0][2] == curz or b[1][2] == curz:
                #move down
                voxels = block_voxels[i]
                world.difference_update(voxels)
                while True:
                    success, voxels = check_level_down(world, voxels)
                    if success:
                        b[0][2] -= 1
                        b[1][2] -= 1
                    else:
                        world.update(voxels)
                        block_voxels[i] = voxels
                        break
    # PART 1
    res = []
    for i, b in enumerate(blocks):
        voxels = block_voxels[i]
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
                
    print('Part 1', len(res))
    
    # PART 2
    res = []
    tops = defaultdict(set)
    bottoms = defaultdict(set)
    for i in block_voxels:
        if (min(blocks[i][0][2], blocks[i][1][2]) == 1):
            continue
        for vy, vx, vz in block_voxels[i]:
            for j in range(len(block_voxels)):
                if i != j:
                    if (vy,vx,vz-1) in block_voxels[j]:
                        tops[j].add(i)
                        bottoms[i].add(j)
                        continue

    part2 = 0
    for i in range(len(block_voxels)):
        to_fall = set()
        to_process = [i]
        to_fall.add(i)
        while to_process:
            j = to_process.pop(0)
            for jj in tops[j]:
                if bottoms[jj] <= to_fall:
                    to_fall.add(jj)
                    to_process.append(jj)
        if (len(to_fall)):
            part2 += len(to_fall) - 1
    print('Part 2', part2)

with open("input/22.txt") as f:
    lines = f.read().rstrip().split('\n')
    input = [[ list(map(int,c1.split(','))), list(map(int,c2.split(',')))]for c1,c2 in (l.split('~') for l in lines)]
    part1(input)