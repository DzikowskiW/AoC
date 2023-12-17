from collections import defaultdict
import numpy as np
import sys
from queue import PriorityQueue

EDGES = ((-1,0), (0,1),(1,0),(0,-1))
MAX_STRAIGHT = 3

def is_maxed_out(y,x,dy,dx, prev_nodes):
    if y == x == 0:
        return False
    node = (y,x)
    
    straights = 0
    i = 1
    while True:
        node = prev_nodes[node[0]][node[1]]
        if node == 0 or node[0] != y - dy*i or node[1] != x - dx*i:
            break
        # print(node[0], dy*i, '|', node[1], x + dx*i)
        straights +=1
        i+=1
    # when someone enters block, they turn next turn, i.e. ^>>>, so it adds up to 4
    return straights > MAX_STRAIGHT
   
   
def kind_of_dijsktra(graph):
    ylen = len(graph)
    xlen = len(graph[0])

    pq = PriorityQueue()
    # dist, coords, , last edge, edge count
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
            ddirlen = 0
            # don't go back
            if last_dir == (-dy, -dx):
                continue
            if last_dir == (dy,dx):
                ddirlen = dirlen + 1
            if ddirlen >= 3:
                continue
            if 0 <= yy < ylen and 0 <= xx < xlen:
                pq.put((dist + graph[yy][xx], (yy,xx), (dy, dx), ddirlen))
    
    res = sys.maxsize
    for (coords, last_dir, dirlen), dist in shortest.items():
        if coords == (ylen-1, xlen-1):
            res = min(res, dist)
    return res

def loop(city):
    return kind_of_dijsktra(city) 
    

with open("input/17.txt") as f:
    lines = f.read().rstrip().split('\n')
    lines = [[int(c) for c in l] for l in lines]
    lines = np.array(lines, dtype=int)
    print('Part 1:', loop(lines))