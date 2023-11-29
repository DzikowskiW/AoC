import numpy as np

def flash(data, i, j, add): 
    if data[i][j] <= 0: return 0
    data[i][j] += add
    if data[i][j] < 10: return 0

    #flash
    data[i][j] = 0
    sum = 1
    for k in range(i-1,i+2):
        for l in range(j-1, j+2):
            if i != k or j != l:
                sum += flash(data, k, l, 1)
    return sum


def p1(a):
    padded = np.pad(a, 1, mode='constant', constant_values=-1)
    maxY, maxX = np.shape(padded)
    sum = 0
    for t in range(100):
        stepSum = 0 
        for i in range(1, maxY-1):
            for j in range(1, maxX-1):
                padded[i][j] += 1
        for i in range(1, maxY-1):
            for j in range(1, maxX-1):
                stepSum += flash(padded, i, j, 0)
        sum += stepSum
    return sum

def p2(a):
    padded = np.pad(a, 1, mode='constant', constant_values=-1)
    maxY, maxX = np.shape(padded)
    t = 0
    while sum(map(sum, padded)) > 0:
        print(t)
        t+=1
        stepSum = 0 
        for i in range(1, maxY-1):
            for j in range(1, maxX-1):
                padded[i][j] += 1
        for i in range(1, maxY-1):
            for j in range(1, maxX-1):
                stepSum += flash(padded, i, j, 0)
    
    return t

            
data = np.genfromtxt('./11.txt', delimiter=1).astype(int)
# print('Part 1: ', p1(data)) 
print('Part 2: ', p2(data)) 
