import aoc
import re
from copy import deepcopy
import math
from collections import defaultdict


def predict(line):
    histories = [[* line]]
    print(histories)
    while not all(map(lambda h: h == 0, histories[-1])):
        histories.append([])
        for i in range(1, len(histories[-2])):
            histories[-1].append(histories[-2][i] - histories[-2][i-1])
        print(histories[-1])
    histories[-1].append(0)
    for i in range(len(histories) -2, -1, -1):
        histories[i].append(histories[i][-1] + histories[i+1][-1])
    print(list(map(lambda l: l[-1], histories)))
    return histories[0][-1]

def part1(lines):
    res= 0
    predict(lines[0])
    for l in lines:
        res += predict(l)
    print(res)
            
        
                

lines = aoc.input_as_lines("input/09a.txt")
lines = [list(map(lambda n: int(n), l.split(' '))) for l in lines]
#part 1
print('part 1:')
part1(lines)

# 1692591070