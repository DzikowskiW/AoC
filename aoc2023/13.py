import aoc
import re
import math
from collections import defaultdict
import numpy as np
from itertools import combinations

def findAxis(shape):
    for i in range(1, len(shape)):
        mirr = True
        size = min(i, len(shape)-i)
        if size == 0:
            continue
        for j in range(size):
            if not np.all(shape[i-j-1] == shape[i+j]):
                mirr = False
                break
        if mirr:
            return i
            # print(i)
            # print(list(range(size)))
            # print(shape[i])
    return 0
        

def loop(shapes):
    summ = 0
    for s in shapes:
        summ += findAxis(s)*100
        summ += findAxis(s.T)
    print(summ)
    

lines = aoc.input_as_lines("input/13.txt")
shapes = [[]]
for l in lines:
    if l == '':
        shapes.append([])
    else:
        shapes[-1].append([*l])

shapes = [np.array(s) for s in shapes]
loop(shapes)