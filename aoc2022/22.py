import re

DIRS_PRINT = ['>', 'v', '<', '^']

DIRS = [ 
        (1, 0), #look right
        (0, 1), #down
        (-1, 0), #left
        (0, -1) #up
    ]

def wrapMap(board, x, y, dir):
    #left 
    xx = -DIRS[dir][0]
    yy = -DIRS[dir][1]
    
    while (x + xx,y + yy) in board:
        x += xx
        y += yy
    
    return x, y

def move(board, path, printb = False):
    y = 0
    x = 0
    dir = 0
    # starting position
    while (x,y) not in board or board[(x,y)] != '.': x +=1
    
    for p in path:
        if p == 'L':
            dir = (dir - 1) % 4
            if printb: board[(x,y)] = DIRS_PRINT[dir]
        elif p == 'R':
            dir = (dir + 1) % 4
            if printb: board[(x,y)] = DIRS_PRINT[dir]
        else: 
            for i in range(p):
                #next 
                nextX = x + DIRS[dir][0]
                nextY = y + DIRS[dir][1]
                # check for edges
                if (nextX, nextY) not in board:
                    #look back and find next
                    nextX, nextY = wrapMap(board, x,y, dir)
                # check for walls
                if board[(nextX, nextY)] == '#':
                    break
                x = nextX
                y = nextY
                if printb: board[(x,y)] = DIRS_PRINT[dir]
    #adjust for 1,1 starting point
    x +=1
    y +=1
    print('END POSITION', x, y, 'direction:', dir, 'result:', 1000*y + 4*x + dir)         
    return 

def printBoard(board, maxX, maxY):
    for y in range(0,maxY):
        line = ''
        for x in range(0,maxX):
            if (x,y) in board:
                line += board[(x,y)]
            else:
                line+= ' '
        print(line)
    print('\n--------------------------\n')

with open("aoc2022/22.txt") as f:
    lines = [x for x in f]
    path = []
    
    board = {}
    maxX = 0
    maxY = len(lines)-2
    for y,l in enumerate(lines):
        if y == len(lines) - 1:
            v = 0
            for c in l:
                if c.isnumeric():
                    v = v * 10 + int(c)
                else:
                    if (v > 0):
                        path.append(v)
                    v = 0
                    path.append(c)
                    
        else:
            for x, c in enumerate(l):
                if c != ' ' and c != '\n':
                    board[(x,y)] = c
                if x > maxX: maxX = x
    print('PART 1')
    move(board, path)  
    # printBoard(board, maxX, maxY)
