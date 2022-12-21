import re
import copy

class Cache:
    dijsktraCache = {}
class Valve: 
    maxMax = 0

    def __init__(self, id, flow, tunnels):
        self.id = id
        self.flow = int(flow)
        self.tunnels = [t for t in tunnels]

    def __repr__(self) -> str:
        r = self.id + ' r:' + str(self.flow) + ' (' + str(self.tunnels)
        return '{' +  r + ')}'

def dijsktra(valves, start):
    if start in Cache.dijsktraCache:
        return Cache.dijsktraCache[start]
    visited = set()
    distances = {}
    distances[start] = 0
    queue = [start]
    while len(queue) > 0:
        vid = queue.pop(0)
        visited.add(vid)
        for tid in valves[vid].tunnels:
            if tid not in distances:
                distances[tid] = distances[vid] + 1
            elif distances[tid] > distances[vid] + 1:
                distances[tid] = distances[vid] + 1
            if tid not in visited:
                queue.append(tid)
    Cache.dijsktraCache[start] = distances
    return distances
                
def bestPath(valves, start, timeLeft, toOpen):
    paths = dijsktra(valves, start)

    maxPaths = []
    for vid in paths:
        if vid not in toOpen:
            continue
        openTime = timeLeft - paths[vid]
        if openTime > 0 and openTime * valves[vid].flow > 0 and vid in toOpen:
            maxPaths.append([vid, paths[vid]])
    return maxPaths


def minuteSearch(valves, vid, vwait, time, flow, toOpen):
    if time == 0:
        return 0
    
    if len(toOpen) == 0:
        return time * flow
        
    # traverse
    if vwait > 0:
        return flow + minuteSearch(valves, vid, vwait - 1, time - 1, flow, toOpen)

    # open
    if vid in toOpen and vwait == 0:
        toOpen.remove(vid)
        return flow + minuteSearch(valves, vid, 0, time - 1, flow + valves[vid].flow, toOpen)
    
    #find nextPath
    maxFlow = 0
    paths = bestPath(valves, vid, time+2, toOpen)
    for p in paths:
        toOpen1 = copy.deepcopy(toOpen)
        nvid = p[0]
        nwait = p[1]
        n = minuteSearch(valves, nvid, nwait, time, flow, toOpen1)
        if n > maxFlow: 
            maxFlow = n

    return maxFlow
    
        
    

def search(valves, vid, time, toOpen):
    if time <= 0  or len(toOpen) == 0:
        return 0

    curFlow = 0
    maxFlow = 0

    #open valve
    if vid in toOpen:
        toOpen.remove(vid)
        time -= 1
        curFlow = time * valves[vid].flow
    
    #get path values to next valves
    paths = bestPath(valves, vid, time,toOpen)

    #traverse
    for p in paths:
        toOpen1 = copy.deepcopy(toOpen)
        nvid = p[0]
        ntime = time - p[1]
        n = search(valves, nvid, ntime, toOpen1)
        if n > maxFlow: 
            maxFlow = n

    maxFlow = curFlow + maxFlow
    # if (maxFlow > Valve.maxMax):
    #     Valve.maxMax = maxFlow
    #     print(Valve.maxMax)
    return maxFlow

with open("aoc2022/16a.txt") as f:
    maxMax = 0
    lines = [x.strip() for x in f]
    valves = {}
    importantV = []
    for line in lines:
        v, f, tt = re.search(r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line).groups()
        valves[v] = Valve(v, f, tt.split(', '))
        if (valves[v].flow > 0):
            importantV.append(v)
    
    #print('Part 1', search(valves, 'AA', 30, importantV))
    print('Part 1 minutte', minuteSearch(valves, 'AA', 0, 30, 0, importantV))
    
    
    