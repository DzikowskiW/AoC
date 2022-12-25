import numpy as np
BLOCKS = [
    [(0,0), (1,0), (2,0), (3,0)],
    [(1,0), (0,1), (1,1), (2,1), (1,2)],
    [(0,0), (1,0), (2,0), (2,1), (2,2)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (0,1), (1,1)]

]
BLOCKS_H = [1,3,3,4,2]
BLOCKS_W = [4,3,3,1,2]

BLOCKS1 = [
np.array([[1,1,1,1]]),
np.array([
    [0,1,0],
    [1,1,1],
    [0,1,0]
]),
np.array([
    [0,0,1],
    [0,0,1],
    [1,1,1]
]),
np.array([[1],[1],[1],[1]]),
np.array([
    [1,1], 
    [1,1]
])
]

def overlaps(x,y,block,stack):
    for b in block:
        if (b[0]+x, b[1]+y) in stack:
            return True
    return False

def moveHorizontal(x,y,dir,block,bx, stack):
    if dir == '<':
        if x == 0: 
            return x, y
        if overlaps(x-1, y, block, stack):
            return x,y
        return x-1, y
    if dir == '>':
        if x+bx == 7: 
            return x, y
        if overlaps(x+1, y, block, stack):
            return x,y
        return x+1, y

def moveDown(x, y, block, by, stack):
    if y == 1:
        return False
    if overlaps(x,y-1,block, stack):
        return False
    return True

def visualise(miny, maxy, stack):
    output = ''
    for y in range(maxy,miny-1,-1):
        line = ''
        for x in range(0,7):
            if (x,y) in stack:
                line += '#'
            else:
                line += '.'
        output += line
    return output

def part2(input, iterations):
    v= len(input)*7*5
    res = tetris(input, iterations % v)
    if (iterations > v):
        v0 = tetris(input, v)
        print(v0)
        v1 = tetris(input, v*2)
        print(v1-v0, v1)
        v2 = tetris(input, v*3)
        print(v2-v1, v2)
        v3 = tetris(input, v*4)
        print(v3-v2, v3)
        v4 = tetris(input, v*5)
        print(v4-v3, v4)
        vv = v2 - v1
    res += vv * int(iterations / v)
    print(res)

def tetris(input, iterations = 2022):
    cache = {}
    maxCombinations = iterations % len(input) * 5
    
    stack = set()
    i = 0
    curBlock = 0
    maxy = 0
    padY = 0
    it = 0 
    useCycle = True
    while it < iterations:
        block = BLOCKS[curBlock]
        bx = BLOCKS_W[curBlock]
        by = BLOCKS_H[curBlock]
        #start place
        x, y = 2, maxy + 4
        
        while True:    
            x, y = moveHorizontal(x, y, input[i], block,bx, stack)
            if moveDown(x, y, block, by, stack):
                y -= 1
            else:
                i = (i+1) % len(input)
                break
            i = (i+1) % len(input)

        # add block 
        for b in block:
            stack.add((b[0]+x, b[1]+y))
        maxy= max(maxy, y+by-1)
        
        #find cycle
        cacheKey = (curBlock, i, visualise(maxy-100,maxy,stack))
        if cacheKey in cache and useCycle:
            cycle = it - cache[cacheKey][0]
            cycleVal = maxy - cache[cacheKey][1]
            padY = ((iterations - it) // cycle)*cycleVal
            it += ((iterations - it) // cycle)*cycle
            useCycle = False
        else:    
            cache[cacheKey] = (it, maxy)
        
        #next block
        curBlock = (curBlock + 1) % len(BLOCKS)
        it += 1
    return maxy + padY


with open("aoc2022/17.txt") as f:
    input = [x.strip() for x in f][0]
    tmp = set()
    print('PART 1')
    print(tetris(input, 2022))
    print('PART 2')
    print(tetris(input, 1000000000000))
    