import aoc
import re
import math
from collections import defaultdict
import numpy as np
from itertools import combinations

PART1_MUL = 2
PART2_MUL = 1000000

def analise(springs, conditions):
    res = 0
    if not '?' in springs:
        # print(conditions, ''.join(springs))
        return 1 if re.match(conditions,''.join(springs)) else 0
    unknown_pos = springs.index('?')
    springs[unknown_pos] = '#'
    res += analise(springs, conditions)
    springs[unknown_pos] = '.'
    res += analise(springs, conditions)
    springs[unknown_pos] = '?'
    return res


def loop(lines):
    summ = 0
    for l in lines:
        springs, conditions = l.split(' ')
        reg = '^\.*'
        for i,c in enumerate(conditions.split(',')):
            if i > 0:
                reg+= '\.+'
            reg += '#{'+c+'}'
        reg += '\.*$'
        # print(l, reg)
        res = analise([*springs], reg)
        summ += res
        # print(res)
    print(summ) 
    

lines = aoc.input_as_lines("input/12.txt")
loop(lines)