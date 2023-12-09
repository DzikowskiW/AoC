import aoc
import re
from copy import deepcopy
import math
from collections import defaultdict

def parseSequence(line):
    seq = [[* line]]
    while not all(map(lambda h: h == 0, seq[-1])):
        seq.append([])
        for i in range(1, len(seq[-2])):
            seq[-1].append(seq[-2][i] - seq[-2][i-1])
    seq[-1].append(0)
    return seq

def predictPrev(line):
    seq = parseSequence(line)
    for i in range(len(seq) -2, -1, -1):
        seq[i].insert(0,seq[i][0] - seq[i+1][0])
    return seq[0][0]

def predictNext(line):
    seq = parseSequence(line)
    for i in range(len(seq) -2, -1, -1):
        seq[i].append(seq[i][-1] + seq[i+1][-1])
    return seq[0][-1]

lines = aoc.input_as_lines("input/09.txt")
lines = [list(map(lambda n: int(n), l.split(' '))) for l in lines]
res= [0,0]
for l in lines:
    res[0] += predictNext(l)
    res[1] += predictPrev(l)
print('part 1, part2:', res)
