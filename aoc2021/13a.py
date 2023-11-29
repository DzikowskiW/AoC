#!/usr/bin/python3

# Day 12, part 1 of Advent of Code 2021

import sys
from collections import defaultdict
import numpy as np

dotsdict = defaultdict(list)
folds = []

with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        if line[0:4] == "fold":
            folds.append([line[11], int(line[13:].strip())])
        elif line.strip() != "":
            x, y = map(int, line.strip().split(","))
            dotsdict[x].append(y)


maxsizey = max(dotsdict.keys()) + 1
maxsizex = max(max(subdict) for subdict in dotsdict.values()) + 1

dots = np.full((maxsizex, maxsizey), False)

for y, xs in dotsdict.items():
    for x in xs:
        dots[x, y] = True

if folds[0][0] == "y":
    belowfold = np.flipud(dots[folds[0][1]+1:, :])
    newpaper = dots[:folds[0][1], :] | belowfold
    print(newpaper.sum())
else:
    belowfold = np.fliplr(dots[:, folds[0][1]+1:])
    newpaper = dots[:, :folds[0][1]] | belowfold
    print(newpaper.sum())