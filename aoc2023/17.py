from collections import defaultdict
import numpy as np
import sys
from queue import PriorityQueue

EDGES = ((-1,0), (0,1),(1,0),(0,-1))
   
def kind_of_dijsktra(graph, part = 1):
    ylen = len(graph)
    xlen = len(graph[0])

    pq = PriorityQueue()
    # dist, coords, last edge, edge count
    pq.put((0, (0,0), -1, -1))    
    shortest = defaultdict(int)
    while not pq.empty():
        dist, coords, last_dir, dirlen = pq.get()
        if (coords,last_dir, dirlen) in shortest:
            continue
        (y, x) = coords
        shortest[(coords,last_dir, dirlen)] = dist
        for dy,dx in EDGES:
            yy = y + dy
            xx = x + dx
            ddirlen = 1
            # don't go back
            if last_dir == (-dy, -dx):
                continue
            if last_dir == (dy,dx):
                ddirlen = dirlen + 1
            if part == 1 and ddirlen > 3:
                continue
            if part == 2 and ddirlen > 10:
                continue
            # same path OK
            # above 4 OK
            #from start OK
            if part == 2 and not (last_dir == (dy,dx) or dirlen >= 4 or coords == (0,0)) :
                continue
            if 0 <= yy < ylen and 0 <= xx < xlen:
                pq.put((dist + graph[yy][xx], (yy,xx), (dy, dx), ddirlen))
    
    res = sys.maxsize
    for (coords, last_dir, dirlen), dist in shortest.items():
        if coords == (ylen-1, xlen-1):
            res = min(res, dist)
    return res

with open("input/17.txt") as f:
    lines = f.read().rstrip().split('\n')
    lines = [[int(c) for c in l] for l in lines]
    city = np.array(lines, dtype=int)
    print('Part 1:', kind_of_dijsktra(city, part=1))    
    print('Part 2:', kind_of_dijsktra(city, part=2))