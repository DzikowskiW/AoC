import numpy as np

E = chr(ord('z')+1)
S = chr(ord('a')-1)
WALL_CHAR = chr(127)
neighbors = [[-1, 0], [1, 0], [0, -1], [0,1]]

def bfs(input1, start, end, cmpr=lambda c,lastc: ord(c) > ord(lastc) + 1):
    input = np.pad(input1, 1, constant_values=WALL_CHAR)
    
    x, y = [n[0] for n in np.where(input == start)]
    visited = np.zeros_like(input, dtype=int)
    visited[:,[0,-1]] = visited[[0,-1]] = 1
    next = [[x,y, 0, None]]
    
    while len(next) > 0:
        x,y, d, lastc = next.pop(0)
        if visited[x][y] > 0:
            continue
        c = input[x,y]
        if lastc is None or cmpr(c, lastc):
            visited[x][y] = d+1
            if input[x][y] == end:
                return d
            for n in neighbors:
                next.append([x + n[0], y + n[1], d+1, c])
    
    assert(False)
   

with open("aoc2022/12.txt") as f:
    input = np.array([[*c] for c in [x.strip() for x in f]])
    
    sx, sy = [n[0] for n in np.where(input == 'S')]
    input[sx,sy] = S
    ex, ey = [n[0] for n in np.where(input == 'E')]
    input[ex,ey] = E
    #part 1
    print('Part 1:', bfs(input, S, E, lambda c,prevc: ord(c) <= ord(prevc) + 1))
    
    #part 2
    sx, sy = [n[0] for n in np.where(input == S)]
    input[sx,sy] = 'a'
    print('Part 2:', bfs(input, E, 'a', lambda c, prevc: ord(prevc) <= ord(c) + 1))

