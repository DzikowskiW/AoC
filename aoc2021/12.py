import numpy as np

def formatGraph(data):
    g = dict()
    for d in data:
        f = d['from']
        t = d['to']
        if  f not in g:
            g[f] = []
        if t not in g:
            g[t] = []
        g[f].append(t)
        g[t].append(f)
    return g

def findPaths(graph, node, paths):
    if node == 'end':
        return 1
    sum = 0
    paths.append(node)
    for p in graph[node]:
        if p.islower() and p in paths:
                continue
        sum += findPaths(graph, p, paths.copy())
    return sum

def findPaths2(graph, node, paths, visited):
    if node == 'end':
        paths.append('end')
        # print(paths)
        return 1
    sum = 0
    paths.append(node)

    if (node.islower()):
        if node not in visited: 
            visited[node] = 0
        visited[node] += 1

    limit = 2
    for el in visited.values():
        if (el > 1): 
            limit = 1
            break

    for p in graph[node]:
        if p =='start': continue
        if p.islower() and p in visited and visited[p] >= limit: continue
        sum += findPaths2(graph, p, paths.copy(), visited.copy())
    return sum

def p1(data):
    return findPaths(data, 'start', [])

def p2(data):
    return findPaths2(data, 'start', [], dict())

            
with open("12.txt") as f:
    lines = [x.strip() for x in f]
    data = []
    for line in lines:
        [fromm, to] = line.split('-')
        data.append({
            'from': fromm,
            'to': to
        })
    data = formatGraph(data)
    #print('Part 1: ', p1(data)) 
    print('Part 2: ', p2(data)) 
