import re
import copy
import numpy

BP_ORE = 0
BP_CLAY_ORE = 1
BP_OBS_ORE = 2
BP_OBS_CLAY = 3
BP_GEO_ORE = 4
BP_GEO_OBS = 5

ORE = 0
CLAY = 1
OBS = 2
GEO = 3

# ore, clay, obsidian, geode
resources = [0,0,0,0]
robots = [1,0,0,0]
class Cache:
    minGeode = 0
    maxGeode = 0
    c = {}
def doFactorio(blueprint, time, resources, robots, robotsTodo=-1):
    if time <= 0:
        return resources[GEO]
    cacheHash = (time,tuple(resources),tuple(robots),tuple(robotsTodo))
    if cacheHash in Cache.c:
        return Cache.c[cacheHash]
    if time < Cache.minGeode and robots[GEO] == 0:
        return 0
    possibilities = []
    #work
    time = time - 1
    for i in range(0,4):
        resources[i] += robots[i]
    
    #make robots
    if robotsTodo >=0:
        robots[robotsTodo] += 1

    #decide what next
    #buy machines
    #geode
    if blueprint[BP_GEO_ORE] <= resources[ORE] and blueprint[BP_GEO_OBS] <= resources[OBS]:
        if time > Cache.minGeode:
            Cache.minGeode = time
            print('t', time)
        resourcesCopy = copy.deepcopy(resources)
        robotsCopy = copy.deepcopy(robots)
        resourcesCopy[ORE] -= blueprint[BP_GEO_ORE]
        resourcesCopy[OBS] -= blueprint[BP_GEO_OBS]
        possibilities.append(doFactorio(blueprint, time, resourcesCopy, robotsCopy, GEO))
    #obsidian
    if blueprint[BP_OBS_ORE] <= resources[ORE] and blueprint[BP_OBS_CLAY] <= resources[CLAY]:
        resourcesCopy = copy.deepcopy(resources)
        robotsCopy = copy.deepcopy(robots)
        resourcesCopy[ORE] -= blueprint[BP_OBS_ORE]
        resourcesCopy[CLAY] -= blueprint[BP_OBS_CLAY]
        robotsCopy[OBS] += 1
        possibilities.append(doFactorio(blueprint, time, resourcesCopy, robotsCopy, OBS))
    #clay
    if (blueprint[BP_CLAY_ORE] <= resources[ORE]):
        resourcesCopy = copy.deepcopy(resources)
        robotsCopy = copy.deepcopy(robots)
        resourcesCopy[ORE] -= blueprint[BP_CLAY_ORE]
        robotsCopy[CLAY] += 1
        possibilities.append(doFactorio(blueprint, time, resourcesCopy, robotsCopy, CLAY)) 
    #ore
    if (blueprint[BP_ORE] <= resources[ORE]):
        resourcesCopy = copy.deepcopy(resources)
        robotsCopy = copy.deepcopy(robots)
        resourcesCopy[ORE] -= blueprint[BP_ORE]
        robotsCopy[ORE] += 1
        possibilities.append(doFactorio(blueprint, time, resourcesCopy, robotsCopy, ORE))
    
    #don't buy
    resourcesCopy = copy.deepcopy(resources)
    robotsCopy = copy.deepcopy(robots)
    possibilities.append(doFactorio(blueprint, time, resourcesCopy, robotsCopy))
    
    maxx = max(possibilities)
    if maxx > Cache.maxGeode:
        Cache.maxGeode = maxx
    Cache.c[cacheHash] = maxx
    return maxx
    
 

with open("aoc2022/19a.txt") as f:
    lines = [x.strip() for x in f]
    blueprints = []
    for line in lines:
        ore, clayOre, obsidianOre, obsidianClay, geodeOre, geodeObsidian = re.search(r"Blueprint \d+:\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+", line).groups()
        blueprint = [ore, clayOre, obsidianOre, obsidianClay, geodeOre, geodeObsidian]
        blueprint = [int(n) for n in blueprint]
        blueprints.append(blueprint)
    
    print(doFactorio(blueprints[0], 24, resources, robots))
    print(blueprints[0])
    
    
    
    