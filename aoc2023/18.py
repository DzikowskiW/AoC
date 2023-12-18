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

#PART 1 - flood fill
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
   
def dehex(h):
    HEX_DIRS = ['R','D', 'L', 'U']
    dir = HEX_DIRS[int(h[-1])]
    n = int(h[1:-1], 16)
    return dir, n
    
#PART 2 - shoelace algorithm (also can be applicable for part 1)  
def shoelace(lines):
    area = 0
    head = (0,0)
    for l in lines:
        _, _, hex_data = l
        dir, n = dehex(hex_data)
        dy = DIRS[dir][0]*n
        dx = DIRS[dir][1]*n
        area += n
        dx = 0 if dx == 0 else dx
        dy = 0 if dy == 0 else dy
        tail = (head[0] + dy, head[1] + dx) 
        area += head[1] * tail[0] - head[0] * tail[1]
        head = tail
    tail = (0,0)
    area += head[1] * tail[0] - head[0] * tail[1]
    area  = int(area/2) + 1 # wut?
    print('part 2:', area)

with open("input/18a.txt") as f:
    lines = f.read().rstrip().split('\n')
    lines = [(ll[0], int(ll[1]), ll[2][1:-1]) for ll in (l.split(" ") for l in lines)]
    loop(lines)
    shoelace(lines)