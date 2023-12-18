from collections import defaultdict
import numpy as np

DIRS = {
    'U': (-1,0),
    'D': (1,0),
    'L': (0,-1),
    'R': (0,1)
}
EMPTY = '.'
FULL = '#'

def flood(canvas, y,x):
    to_fill = set([(y,x)])
    while to_fill:
        yy, xx = to_fill.pop()
        if canvas[yy][xx] == FULL:
            continue
        canvas[yy][xx] = FULL
        for e in DIRS.values():
            next_val = (yy + e[0], xx + e[1])
            if canvas[next_val] == EMPTY:
                to_fill.add(next_val)
    return canvas

def loop(lines):
    #arbitrary params
    ylen = 300
    xlen = 900
    head = (80,10)

    canvas = np.full((ylen, xlen), EMPTY, dtype=str)
    canvas[head] = FULL
    #shape
    for l in lines:
        dir, n, color = l
        for _ in range(1,n+1):
            head = (head[0] + DIRS[dir][0], head[1] + DIRS[dir][1])
            assert(head[0] >=0 and head[1] >= 0)
            canvas[head] = FULL
    flood(canvas, head[0]+1, head[1]+1)
    np.savetxt("./output/tmp.txt", canvas, fmt='%s',delimiter='')
    print('part 1:', (canvas == FULL).sum())        
   
with open("input/18.txt") as f:
    lines = f.read().rstrip().split('\n')
    lines = [(ll[0], int(ll[1]), ll[2][1:-1]) for ll in (l.split(" ") for l in lines)]
    loop(lines)