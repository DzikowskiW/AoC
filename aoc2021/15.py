from more_itertools import interleave_longest, windowed
from collections import Counter
from queue import PriorityQueue
import numpy as np



def dijsktra(graph):
    shortest = np.full((len(graph), len(graph[0])), -1)
    visited = np.zeros((len(graph), len(graph[0])))
    pq = PriorityQueue()
    pq.put((0, (0,0)))
    shortest[0][0] = 0

    while not pq.empty():
        (dist, coords) = pq.get()
        (y, x) = coords
        # print('p', y, x,'dist:', dist)
        visited[y][x] = 1
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if i < 0 or j < 0 or i >= len(graph) or j >= len(graph[0]): 
                    continue
                if i != y and j != x: 
                    continue
                if visited[i][j] == 0:
                    newPath = shortest[y][x] + graph[i][j]
                    oldPath = shortest[i][j]
                    if newPath < oldPath or shortest[i][j] == -1:
                        shortest[i][j] = newPath
                        pq.put((newPath, (i,j)))
        
    return shortest[len(shortest)-1][len(shortest[0])-1]

def p1(graph):
    return dijsktra(graph)

def p2(graph):
    newGraph = np.zeros((len(graph)*5, len(graph[0])*5), dtype=int)
    print((len(graph)*5, len(graph[0])*5))
    yLen = len(graph)
    xLen = len(graph[0])
    for y in range(len(newGraph)):
        for x in range(len(newGraph[0])):
            yFrom = y if y < yLen else y - yLen
            xFrom = x if x < xLen else x - xLen
            if y < yLen and x < xLen:
                newGraph[y][x] = graph[y][x]
            elif y < yLen:
                newGraph[y][x] = (newGraph[y][x - xLen] + 1) % 10
            elif x < xLen:
                newGraph[y][x] = (newGraph[y - yLen][x] + 1) % 10
            else: 
                newGraph[y][x] = (newGraph[y - yLen][x] + 1) % 10
            if newGraph[y][x] == 0:
                newGraph[y][x] = 1
    
    # #print
    # for y in newGraph:
    #     s = ''
    #     for x in y:
    #         s+= str(x)
    #     print(s)
    return dijsktra(newGraph)


graph = np.genfromtxt('./15.txt', delimiter=1).astype(int)
# print('P1', p1(graph)) 
print('P2', p2(graph))