import numpy as np

def calcIfMin(data, i, j):
    if data[i-1][j] <= data[i][j]: return False
    if data[i+1][j] <= data[i][j]: return False
    if data[i][j-1] <= data[i][j]: return False
    if data[i][j+1] <= data[i][j]: return False
    return True

def p1(a):
    padded = np.pad(a, 1, mode='constant', constant_values=10)
    sum = 0
    sinks = 0
    maxY, maxX = np.shape(padded)
    for y in range(1, maxY-1):
        for x in range(1, maxX-1):
            if calcIfMin(padded, y, x):
                sum += padded[y][x] + 1
                sinks += 1
    return sum

def calcSink(data, i, j, cache):
    if data[i][j] >= 9: return 0
    cacheKey = str(i)+','+str(j)
    if cacheKey in cache: return 0
    cache[cacheKey] = 1
    return 1 + calcSink(data, i-1, j, cache) + calcSink(data, i+1, j, cache) + calcSink(data, i, j+1, cache) + calcSink(data, i, j-1, cache)

def p2(a):
    padded = np.pad(a, 1, mode='constant', constant_values=10)
    sum = 0
    sinks = []
    maxY, maxX = np.shape(padded)
    for y in range(1, maxY-1):
        for x in range(1, maxX-1):
            if calcIfMin(padded, y, x):
                sinks.append(calcSink(padded, y, x, dict()))
               # sinks.append((y,x,calcSink(padded, y, x, dict())))
    sinks.sort(reverse=True)
    return sinks[0] * sinks[1] * sinks[2]
            
data = np.genfromtxt('./09.txt', delimiter=1).astype(int)
# print('Part 1: ', p1(data)) #629, 252 sinks
print('Part 2: ', p2(data))