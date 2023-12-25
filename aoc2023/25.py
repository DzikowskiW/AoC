import numpy as np
from collections import defaultdict
from heapq import heappop, heappush
import functools
from copy import deepcopy
from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt

def process(lines):
    graph = defaultdict(set)
    G = nx.Graph()
    for fr, tos in lines:
        for to in tos:
            if fr not in graph:
                G.add_node(fr)
            if to not in graph:
                G.add_node(fr)
            if to not in graph[fr]:
                G.add_edge(fr, to)
            graph[fr].add(to)
            graph[to].add(fr)
            
    sizes = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    print('part1:', sizes[0]*sizes[1], sizes)
    
    # analize graph to cut out 3 wires
    # nx.draw(G, with_labels=True, font_size=8)
    # plt.savefig("output/25.png")
    #vtv kkp
    #cmj qhd
    #lnf jll

with open("input/25.txt") as f:
    lines = f.read().rstrip().split('\n')
    lines = [(ll, lr.split(' ')) for ll, lr in (l.split(': ') for l in lines)]
    
    process(lines)