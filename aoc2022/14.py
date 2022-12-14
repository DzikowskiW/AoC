import numpy as np

SANDSTART_CHAR = '+'
LIMIT_CHAR = '🪨'
EMPTY_CHAR = '.'
LINE_CHAR = '#'
SAND_CHAR = 'O'

def prepareCave(lines, minX, maxX, maxY):
    caveWidth = maxX - minX + 1
    cave = np.full((caveWidth, maxY+1),EMPTY_CHAR, dtype=str)
    for l in lines:
        f = l.pop(0)
        while len(l) > 0:
            t = l.pop(0)
            minXX = min(t[0], f[0]) - minX
            maxXX = max(t[0], f[0]) - minX
            minYY = min(t[1], f[1])
            maxYY = max(t[1], f[1])
            for xx in range(minXX, maxXX+1):
                for yy in range(minYY, maxYY+1):
                    cave[xx][yy] = LINE_CHAR
            f = t
    
    sandX = 500 - minX
    cave[sandX][0] = SANDSTART_CHAR
    
    cave = np.pad(cave, 1, constant_values=LIMIT_CHAR)
    return cave

def printCave(cave):
    print(np.transpose(cave))
    
def makeSand(cave):
    sandY = 1
    sandX = np.where(cave == SANDSTART_CHAR)[0][0]
    sands = 0
    while addSand(cave, sandX, sandY):
        sands += 1
        print(sands)
        if (sands == 843):
            printCave(cave)
    #printCave(cave)
    print(sands)

def addSand(cave, sandX, sandY):
    x = sandX
    y = sandY
    while (True):
        print(x,y)
        if (cave[x, y+1] == EMPTY_CHAR):
            y += 1
        elif (cave[x, y+1] == LIMIT_CHAR):
            return False
        elif cave[x,y+1] in [LINE_CHAR, SAND_CHAR]:
            if cave[x-1,y+1] == EMPTY_CHAR:
                y += 1
                x -= 1
                continue
            if cave[x+1,y+1] == EMPTY_CHAR:
                x += 1
                y += 1
                continue
            if cave[x+1,y+1] == LIMIT_CHAR or cave[x-1,y+1] == LIMIT_CHAR:
                return False
            break
        else: 
            assert(False)
            
    if cave[x][y] == EMPTY_CHAR:
        cave[x][y] = SAND_CHAR
        return True
    else:
        return False
        

with open("aoc2022/14.txt") as f:
    input = [x.strip() for x in f]
    lines = []
    minX = 1000
    maxX = 0
    maxY = 0
    for line in input:
        l = []
        for point in line.split(' -> '):
            p = [int(i) for i in point.split(',')]
            l.append(p)
            if p[0] < minX: minX = p[0]
            if p[0] > maxX: maxX = p[0]
            if p[1] > maxY: maxY = p[1]
        lines.append(l)
        
    cave = prepareCave(lines, minX, maxX, maxY)
    #printCave(cave)
    makeSand(cave)
        
        
