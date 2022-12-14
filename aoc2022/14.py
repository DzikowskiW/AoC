import numpy as np

SANDSTART_CHAR = '➕'
LIMIT_CHAR = '🪨'
EMPTY_CHAR = '⚫'
LINE_CHAR = '🟤'
SAND_CHAR = '🟡'

def plotCave(lines, minX, maxX, maxY):
    caveWidth = maxX - minX + 1
    cave = np.full((caveWidth, maxY+1),EMPTY_CHAR, dtype=str)
    for l in lines:
        f = l[0]
        for i in range(1,len(l)):
            t = l[i]
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
    c = np.transpose(cave)
    for l in c:
        print(''.join(l))
    
def dripSand(cave):
    sandY = 1
    sandX = np.where(cave == SANDSTART_CHAR)[0][0]
    sands = 0
    
    while addSand(cave, sandX, sandY):
        sands += 1

    print('Units of sand', sands)

def addSand(cave, sandX, sandY):
    x = sandX
    y = sandY
    if (cave[sandX, sandY] != SANDSTART_CHAR):
        return False
    
    while (True):
        if (cave[x, y+1] == EMPTY_CHAR):
            # go down
            y += 1
        elif (cave[x, y+1] == LIMIT_CHAR):
            #bottomless pit
            return False
        else:
            # go down left
            if cave[x-1, y+1] == EMPTY_CHAR:
                y += 1
                x -= 1
                continue
            
            #go down right
            if cave[x+1,y+1] == EMPTY_CHAR:
                x += 1
                y += 1
                continue
            
            #bottomless pit 
            if cave[x+1,y+1] == LIMIT_CHAR or cave[x-1,y+1] == LIMIT_CHAR:
                return False
            
            #no way yo go, stay at x,y
            break
            
    if cave[x][y] in [EMPTY_CHAR, SANDSTART_CHAR]:
        cave[x][y] = SAND_CHAR
        return True
    else:
        assert(False)
        

with open("aoc2022/14a.txt") as f:
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
        
    print('PART 1')
    cave = plotCave(lines, minX, maxX, maxY)
    dripSand(cave)
    printCave(cave)
    
    cave = plotCave(lines, 0, maxX+1000, maxY+1)
    cave[:,cave.shape[1]-1] = LINE_CHAR
    print('PART 2')
    dripSand(cave)
    # printCave(cavePart2)

        
