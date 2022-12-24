import numpy as np

BLOCKS = [
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

def moveHorizontal(x,y,dir,block, stack):
    by, bx = block.shape
    sy, sx = stack.shape
    if dir == '<':
        if x == 0: 
            return x, y
        if np.count_nonzero(stack[y:y+by, x-1:x-1+bx] & block) > 0:
            return x,y
        return x-1, y
    if dir == '>':
        if x+bx == sx: 
            return x, y
        if np.count_nonzero(stack[y:y+by, x+1:x+1+bx] & block) > 0:
            return x,y
        return x+1, y

def moveDown(x,y,block, stack):
    by, bx = block.shape
    sy, sx = stack.shape
    if y+by == sy: 
        return False
    if np.count_nonzero(stack[y+1:y+by+1, x:x+bx] & block) > 0:
        return False
    return True

def visualise(miny, maxy, stack,block):
    cut = stack[miny:maxy][:]
    cy,cx = cut.shape
    for y in range(0, cy):
        line = ''
        for x in range(0,cx):
            if cut[y,x] == 1: line += '#'
            if cut[y,x] == 0: line += '.'
        print(line)
    

def part1(input):
    stack = np.zeros((5000, 7), dtype=int)
    sy, sx = stack.shape
    i = 0
    curBlock = 0
    topy = sy
    for it in range(0, 2022):

        block = BLOCKS[curBlock]
        by, bx = block.shape
        #start place
        x, y = 2, topy - 3 - by
        
        while True:    
            x, y = moveHorizontal(x, y, input[i], block, stack)
            if moveDown(x, y, block, stack):
                y += 1
            else:
                i = (i+1) % len(input)
                break
            i = (i+1) % len(input)

        # add block 
        for xx in range(0, bx):
            for yy in range(0, by):
                stack[y + yy, x + xx] = max(block[yy,xx], stack[y + yy, x + xx])
        topy = min(topy, y)
        #next block
        curBlock = (curBlock + 1) % len(BLOCKS)
    print('height', sy-topy)


with open("aoc2022/17.txt") as f:
    input = [x.strip() for x in f][0]
    part1(input)