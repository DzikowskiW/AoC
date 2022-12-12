import numpy as np


def bfs(input, sx, sy, end = 'E'):
    x = sx
    y = sy
    smallest = -1
    visited = np.zeros_like(input, dtype=int)
    xlen, ylen = input.shape
    next = [[sx,sy, 0, None]]
    while len(next) > 0:
        x,y, d, lastc = next.pop(0)
        if x < 0 or x >= xlen or y < 0 or y >= ylen:
            continue
        if visited[x][y] > 0:
            continue
        c = input[x,y]
        if c == 'S': c = chr(ord('a')-1)
        if lastc is not None and input[x,y] != end and ord(c) > ord(lastc) + 1:
            continue
        if lastc != 'z' and input[x,y] == end:
            continue
        visited[x][y] = d+1
        if input[x][y] == end:
            return d
        next.append([x-1, y, d+1, c])
        next.append([x+1, y, d+1, c])
        next.append([x, y-1, d+1, c])
        next.append([x, y+1, d+1, c])
    
    return 0


def calc(input):
    #find start
    sx, sy = [n[0] for n in np.where(input == 'S')]

    #bfs
    return bfs(input, sx, sy, 'E')

def calcPart2(input):
    sx, sy = [n[0] for n in np.where(input == 'S')]
    input[sx,sy] = 'a'
    
    res = []
    xlen, ylen = input.shape
    for xx in range(0,xlen):
        for yy in range(0, ylen):
            if (input[xx, yy] == 'a'):
                path = bfs(input, xx, yy, 'E')
                if (path > 0):
                    res.append(path)
        
    #bfs
    return min(res)


with open("aoc2022/12.txt") as f:
    input = np.array([[*c] for c in [x.strip() for x in f]])

    print('part 1', calc(input))
    print('part 2', calcPart2(input))

