import numpy as np
from collections import defaultdict
from heapq import heappop, heappush
import functools
from copy import deepcopy

START = (0,1)
EDGES = [(-1, 0, '^'), (0,1,'>'), (1, 0, 'v'), (0, -1, '<')]

def topo_sort(mapp, start = START):
    ylen = len(mapp)
    xlen = len(mapp[0])
    
    #make tree
    vertices = set()
    #edge =  dist, (y,x)
    edges_to = defaultdict(list)
    edges_from = defaultdict(list)
    perms = set()
    temps = set()
    topo = []
    vertices.add(start)
    
    #map vertices (point, from_vertex, dist)
    to_check = [(start[0], start[1], start[0], start[1], -1)]
    visited = set()
    while to_check:
        y,x,fy,fx, dist = to_check.pop(0)
        if (y,x,fy,fx) in temps:
            continue
        temps.add((y,x,fy,fx))
        dist += 1
        edges = []
        edge_count = 0
        for dy, dx, slope in EDGES:
            ny, nx = y + dy, x + dx
            if 0 <= ny < ylen and 0 <= nx < xlen:     
                if mapp[ny][nx] in ['.', '<','>','v', '^']:
                    edge_count += 1
                if mapp[ny][nx] in ['.', slope]:
                    edges.append((ny,nx))
        if edge_count != 2:
            vertices.add((y,x))
            if (y,x) != (fy,fx):
                edges_from[(fy,fx)].append((dist,(y,x)))
                edges_to[(y,x)].append((dist,(fy,fx)))
                dist = 0
                fy,fx = y,x
        for e in edges:
            to_check.append((e[0],e[1], fy,fx, dist))
    
    #do the topo
    temps = set()
    def dfs(y,x):
        if (y,x) in perms:
            return
        if (y,x) in temps:
            assert(False)
        temps.add((y,x))
        for e in edges_from[(y,x)]:
            _, (ny, nx) = e
            dfs(ny, nx)
        temps.remove((y,x))
        topo.insert(0,(y,x))
    dfs(*start)
    
    longest = defaultdict(int)
    
    #find the longest
    for _ in topo:
        for u in topo:
            uy, ux = u
            for dist, v in edges_from[u]:
                if (longest[v] < longest[u] + dist):
                    longest[v] = longest[u] + dist

    # p(mapp)            
    # p(mapp, vertices)  
    # print(len(vertices))
    # print(vertices)       
    # print(edges_from)
    # print(topo)
    print('part1:', longest[(ylen - 1, xlen - 2)])



def p(mapp, points = set(), symbol = 'O'):
    print('-'*80)
    for y, l in enumerate(mapp):
        s = []
        for x,l in enumerate(list(l)):
            if (y,x) in points:
                s.append(symbol)
            else:
                s.append(l)     
        print(' '.join(s))


with open("input/23.txt") as f:
    lines = f.read().rstrip().split('\n')
    topo_sort(lines)