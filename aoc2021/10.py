import operator
import functools
import copy
import math
from collections import defaultdict

prents = {
    '{' : '}',
    '(': ')',
    '<': '>',
    '[': ']'
}
p1points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
p2points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def parse(s):
    stack = []
    sum = 0
    for c in s:
        if c in ['{', '(', '<', '[']:
            stack.append(c)
        elif c in ['}', ')', '>', ']']:
            ch = stack.pop()
            if prents[ch] != c:
                print('wr', ch, c, p1points[c])
                sum += p1points[c]
        else:
            print('invalid', c)
            assert(False)
    return sum

def complete(s):
    stack = []
    sum = 0
    for c in s:
        if c in ['{', '(', '<', '[']:
            stack.append(c)
        elif c in ['}', ')', '>', ']']:
            ch = stack.pop()
            if prents[ch] != c:
                return 0
        else:
            print('invalid', c)
            assert(False)
    while len(stack) > 0:
        c = stack.pop()
        sum = 5 * sum + p2points[prents[c]] 

    # print(sum)
    return sum


def p1(subsystem):
    sum = 0
    for s in subsystem:
        sum += parse(s)
    print('SUM,', sum)

def p2(subsystem):
    sums = []
    for s in subsystem:
        res = complete(s)
        if res > 0:
            sums.append(res)
    #print(len(sums) / 2)
    sums.sort()
    print('SUM2', sums[math.floor(len(sums) / 2)])



with open("10.txt") as f:
    lines = [x.strip() for x in f]
    subsystem = []
    for line in lines:
        subsystem.append(list(line))
    p2(subsystem)