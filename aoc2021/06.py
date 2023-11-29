import operator
import functools
import copy
from collections import defaultdict


def p1(fish, days):
    newFish = []
    for d in range(days):
        l = len(fish)
        for i in range(l):
            if fish[i] == 0:
                fish.append(8)
                fish[i] = 6
            else:
                fish[i] -= 1
    
    # print(fish)
    print('total p1: ', len(fish))

def p2(fish, days):
    daysFish = [0,0,0,0,0,0,0,0,0]

    #map fish
    for f in fish:
        daysFish[f] += 1

    #loop days
    for d in range(0, days):
        today = daysFish.pop(0)
        daysFish[6] += today
        daysFish.append(today)
    
    print('total p2: ', functools.reduce(lambda a,b : a + b, daysFish, 0))


with open("06.txt") as f:
    lines = [x.strip() for x in f]
    fish = map(lambda val : int(val), lines[0].split(','))
   
    # p1(copy.deepcopy(fish), 80)
    p2(fish, 256)

