import re
import copy
import numpy as np

ORE = 3
CLAY = 2
OBS = 1
GEO = 0
MAX_POSSIBILITIES = 100

key = lambda a: tuple(a[0]+a[1]) + tuple(a[1])
prune = lambda x: sorted({key(x):x for x in x}.values(), key=key)[-1000:]
    
def nparr(*a):
     return np.array(a, dtype=int)
 
def deduplicatePossibilities(possibilities):
    posSet = set()
    dedup = []
    for resources, robots in possibilities:
        key = (tuple(resources), tuple(robots))
        if key not in posSet:
            dedup.append((resources, robots))
            posSet.add(key)

    #assume that the best candidate is within MAX_POSSIBILITIES best
    dedup = sorted(dedup, key=lambda t: tuple(t[0] + t[1]))
    return dedup[-MAX_POSSIBILITIES:]
    
def doFactorio(blueprint, time):
    possibilities = [(nparr(0,0,0,0), nparr(0,0,0,1))]
    for minute in range(time, 0, -1):
        nextPossibilities = []
        for resources, robots in possibilities:
            #check if we can make robots
            if all(blueprint[GEO] <= resources):
                nextPossibilities.append([resources - blueprint[GEO] + robots, robots + nparr(1,0,0,0)])
            if all(blueprint[OBS] <= resources):
                nextPossibilities.append([resources - blueprint[OBS] + robots, robots + nparr(0,1,0,0)])
            if all(blueprint[CLAY] <= resources):
                nextPossibilities.append([resources - blueprint[CLAY] + robots, robots + nparr(0,0,1,0)])
            if all(blueprint[ORE] <= resources):
                nextPossibilities.append([resources - blueprint[ORE] + robots, robots + nparr(0,0,0,1)])
            #produce resources
            nextPossibilities.append([resources + robots, robots])
        possibilities = deduplicatePossibilities(nextPossibilities)
        
    return max(resources[GEO] for resources, _ in possibilities)

with open("aoc2022/19.txt") as f:
    lines = [x.strip() for x in f]
    blueprints = []
    res = []
    part1 = 0
    part2 = 1
    for line in lines:
        id, ore, clayOre, obsidianOre, obsidianClay, geodeOre, geodeObsidian = re.search(r"Blueprint (\d+):\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+", line).groups()
        id = int(id)
        blueprint = nparr(
            nparr(0, geodeObsidian, 0, geodeOre),
            nparr(0,0, obsidianClay, obsidianOre),
            nparr(0, 0, 0, clayOre),
            nparr(0,0,0,ore),
        )
        blueprints.append(blueprint)
        part1 += id * doFactorio(blueprint, 24)
        if id < 4:
            part2 *= doFactorio(blueprint, 32)
    print('Part 1:', part1)
    print('Part 2:', part2)
    
    
    
    