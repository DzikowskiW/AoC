import aoc
import functools
import re
import math
from collections import defaultdict

def loop1(seeds, lines):
    res = 0
    nextSteps = {}
    curStep = ''
    nextStep = ''
    types = defaultdict(list)
    for i, line in enumerate(lines):
        if len(line) == 0:
            curStep = ''
        elif curStep == '':
            curStep, nextStep = line.split(' ')[0].split('-to-')
            nextSteps[curStep] = nextStep
        else:
            dest, src, l = list(map(int, line.split(' ')))
            types[curStep].append((src,dest,l))
    
    minLocation =  math.inf
    for s in seeds:
        nextVal = s
        t = 'seed'
        while t in nextSteps:
            for src, dest, l in types[t]:
                if nextVal >= src and nextVal < src + l:
                    nextVal = dest + (nextVal - src)
                    break
            t = nextSteps[t]
        minLocation = min(nextVal, minLocation)
    print('part 1:', minLocation)
    
def in_seed_range(n, range):
    for r in range:
        if r[0]<= n and r[1]> n:
            return True    
    return False

def loop2(seeds, lines):
    # seed ranges
    seed_ranges = []
    for i in range(0, len(seeds)-1, 2):
        seed_ranges.append((seeds[i], seeds[i]+seeds[i+1]))
    seed_ranges = sorted(seed_ranges)
    
    prevSteps = {}
    curStep = ''
    nextStep = ''
    types = defaultdict(list)
    for line in lines:
        if len(line) == 0:
            curStep = ''
        elif curStep == '':
            curStep, nextStep = line.split(' ')[0].split('-to-')
            prevSteps[nextStep] = curStep
        else:
            dest, src, l = list(map(int, line.split(' ')))
            types[curStep].append((dest,src,l))
    
    ii = 0
    while True:
        t = 'location'
        res = ii
        while True:
            for src, dest, l in types[t]:
                if res >= src and res < src + l:
                    res = dest + (res - src)
                    break
            if t not in prevSteps:
                break;
            t = prevSteps[t]
        if in_seed_range(res, seed_ranges): 
            print('part2', ii)
            return
        ii += 1

        
lines = aoc.input_as_lines("input/05.txt")
seeds = list(map(int,re.findall(r'\d+', lines[0])))
lines = lines[2:]
loop1(seeds, lines)
loop2(seeds, lines)