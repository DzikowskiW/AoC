import operator
import functools
import copy
from collections import defaultdict

def calcDist(a, b):
    dist = abs(a-b)
    return functools.reduce(lambda sum, val: sum + val, [*range(dist+1)], 0)

def p1(positions):
    maxx = max(positions)
    minCost = -1
    for i in range(maxx):
        cost = functools.reduce(lambda c, val: c + abs(val - i), positions, 0)
        if minCost == -1 or cost < minCost:
            minCost = cost
    print('total p1: ', minCost)

def p2(positions):
    maxx = max(positions)
    minCost = -1
    for i in range(maxx):
        cost = functools.reduce(lambda c, val: c + calcDist(val, i), positions, 0)
        print(i, minCost)
        if minCost == -1 or cost < minCost:
            minCost = cost
    print('total p2: ', minCost)


with open("07.txt") as f:
    lines = [x.strip() for x in f]
    positions = [*map(lambda val : int(val), lines[0].split(','))]
    p2(positions)

#105084264