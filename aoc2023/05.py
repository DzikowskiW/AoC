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
            # for j in range(l):
            #     types[curStep][src +j] = dest + j 
        print('aa')
    
    print('minLoc')
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
        print(t, nextVal)
        minLocation = min(nextVal, minLocation)
    
    # print(nexśtSteps['seed'], types['seed'][0])
    print('part 1:', minLocation)
        
lines = aoc.input_as_lines("input/05.txt")
seeds = list(map(int,re.findall(r'\d+', lines[0])))
lines = lines[2:]
loop1(seeds, lines)
