import re

def posToCheck(elf, elves, dir):
    n = (elf[0]-1, elf[1])
    ne = (elf[0]-1, elf[1]+1)
    nw = (elf[0]-1, elf[1]-1)
    
    e = (elf[0], elf[1]+1)
    w = (elf[0], elf[1]-1)
        
    s = (elf[0]+1, elf[1])
    se = (elf[0]+1, elf[1]+1)
    sw = (elf[0]+1, elf[1]-1)
    
    if not any(pos in elves for pos in [n, ne, nw, e, w, s, se, sw]):
        return elf
        
    if dir == 'N':
        if not (n in elves or ne in elves or nw in elves):
            return n
    elif dir == 'S':
        if not (s in elves or se in elves or sw in elves):
            return s
    elif dir == 'W':
        if not (w in elves or sw in elves or nw in elves):
            return w
    elif dir == 'E':
        if not (e in elves or se in elves or ne in elves):
            return e
    return None

def moveTimes(times, elves):
    dirs = ['N', 'S', 'W', 'E']
    for t in range(times):
        # print('\nIteration ', t+1, dirs)
        elves = move(elves, dirs)
        dir = dirs.pop(0)
        dirs.append(dir)
        # printElves(elves)
    calcPart1(elves)
    return elves

def move(elves, dirs):
    possible = {}
    nextElves = {}
    for e in elves:
        for dir in dirs:
            nextPos = posToCheck(e, elves, dir)
            if nextPos is not None: 
                break
        
        if nextPos == None:
            nextPos = e
        nextElves[e] = nextPos
            
        if nextPos in possible:
            possible[nextPos] += 1
        else:
            possible[nextPos] = 1
            
    ee = {}
    for e in elves:
        if possible[nextElves[e]] > 1:
            ee[e] = '#'
        else: 
            ee[nextElves[e]] = '#'
            
    return ee
        
def calcPart1(elves):
    minX = 10000
    maxX = -10000
    minY = 10000
    maxY = -10000
    for e in elves:
        minX = min(minX, e[1])
        maxX = max(maxX, e[1])
        minY = min(minY, e[0])
        maxY = max(maxY, e[0])
    rect = (maxX-minX)*(maxY-minY)
    print('part 1', rect)

def printElves(elves):
    minX = 10000
    maxX = -10000
    minY = 10000
    maxY = -10000
    for e in elves:
        minX = min(minX, e[1])
        maxX = max(maxX, e[1])
        minY = min(minY, e[0])
        maxY = max(maxY, e[0])
    s = ''
    for y in range(minY, maxY+1):
        for x in range(minX, maxX+1):
            if (y,x) in elves:
                s += '#'
            else:
                s += '.'
        s += '\n'
    print(s)


with open("aoc2022/23.txt") as f:
    lines = [x for x in f]    
    elves = {}
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == '#':
                elves[(y, x)] = '#'
    
    printElves(moveTimes(10, elves))
       