import numpy as np
from collections import defaultdict
import functools

def score(lines):
    score = 0
    ylen = len(lines)
    xlen = len(lines[0])
    for i in range(ylen):
        for j in range(xlen):
            if lines[i][j] == 'O':
                score += ylen - i
    return score

# @functools.cache
def tilt(lines):
    ylen = len(lines)
    xlen = len(lines[0])
    for _ in range(1, ylen):
        for y in range(1, ylen):
            for x in range(xlen):
                if lines[y-1][x] == '.' and lines[y][x] == 'O':
                    lines[y-1][x] = 'O'
                    lines[y][x] = '.' 
    return lines
    
def pretty_print(lines):
    print('\n------------')
    for l in lines:
        print(''.join(list(map(str,l))))
    # print(score(lines))

def loop2(lines):
    # pretty_print(lines)
    last_scores = defaultdict(int)
    scores_count = defaultdict(int)
    for it in range(1,1000):   
        for _ in range(4):
            lines = tilt(lines)
            lines = np.rot90(lines, 3)
        scr = score(lines)
        last_scores[scr] = it - last_scores[scr]
        scores_count[scr] += 1
        if it % 10 == 0:
            print(str(it),': ', score(lines), 'last:', last_scores[scr])
            print(sorted(scores_count.items(), key=lambda x:x[1], reverse=True))
        # pretty_print(lines)
        # print('ITER ', it+1)
    print(sorted(scores_count.items(), key=lambda x:x[1], reverse=True))

def loop(lines):
    lines = tilt(lines)
    pretty_print(lines)
    
# print(rotate([[1,2,3], [4,5,6], [7,8,9]]))

with open("input/14.txt") as f:
    input = f.read().rstrip("\n").split("\n\n")
    input = [[[*l] for l in ll.split("\n")] for ll in input]
    input = [np.array(s) for s in input]
    loop2(input[0])
    
 