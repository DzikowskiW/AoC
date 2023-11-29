import operator
import math
from collections import defaultdict

inta = ord('a')
intA = ord('A')

def letterToVal(c):
    cint = ord(c)
    if cint >= inta:
            cint = cint-inta + 1
    else:
        cint = cint-intA + 27
    return cint

def loop(lines):
    part1 =  0
    part2 = 0
    for line in lines:
        pivot = math.floor(len(line) / 2)
        c1 = list(line[:pivot])
        c2 = list(line[pivot:])
        common = set(c1) & set(c2)
        for c in common:
            part1 += letterToVal(c)
    print(part1)

def loopP2(lines):
    res =  0
    vals = []
    threes = []
    sum = 0
    for i in range(0, len(lines), 3):
        three = []
        for line in lines[i: i + 3]:
            three.append(''.join(sorted(''.join(set(line)))))
        s = ''.join(sorted(three[0]+three[1]+three[2]))
        count = 0
        prev = 0
        for c in s:
            if prev == c:
                count += 1
            else:
                count = 1
            if count > 2:
                print('RES', c)
                sum += letterToVal(c)
                break
            prev = c

    print(sum)
        

    print(threes)


with open("03.txt") as f:
    lines = [x.strip() for x in f]

    loop(lines)


