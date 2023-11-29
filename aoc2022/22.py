import re

DIRS_PRINT = ['>', 'v', '<', '^']
EDGE = 50

R = 0
B = 1
D = 1
L = 2
T = 3
U = 3

DIRS = [ 
        (1, 0), #look right
        (0, 1), #down
        (-1, 0), #left
        (0, -1) #up
    ]
    
def assert3D(board):
    assertPrint(board, (8, 0, L), (4, 4, D)) # 2,0 L
    assertPrint(board, (8, 3, L), (7, 4, D)) # 2,0 L
    assertPrint(board, (8, 0, T), (3, 4, D)) # 2,0 T
    assertPrint(board, (11, 0, T), (0, 4, D)) # 2,0 T
    assertPrint(board, (11, 0, R), (15, 11, L)) # 2,0 R
    assertPrint(board, (11, 3, R), (15, 8, L)) # 2,0 R
    assertPrint(board, (11, 4, R), (15, 8, D)) # 2,1 R
    assertPrint(board, (11, 7, R), (12, 8, D)) # 2,1 R
    assertPrint(board, (12, 8, T), (11, 7, L)) # 3,2,T
    assertPrint(board, (15, 8, T), (11, 4, L)) # 3,2,T
    assertPrint(board, (15, 8, T), (11, 4, L)) # 3,2,T
    assertPrint(board, (15, 8, T), (11, 4, L)) # 3,2,T

def assertPrint(board, l, r):
    print(wrapCube(board, *l), r)
    assert(wrapCube(board, *l) == r)
    
def wrapMap(board, x, y, dir):
    xx = -DIRS[dir][0]
    yy = -DIRS[dir][1]
    
    while (x + xx,y + yy) in board:
        x += xx
        y += yy
    
    return x, y

def wrapCube(x,y,dir):
    R = 0
    B = 1
    D = 1
    L = 2
    T = 3
    U = 3

    xreg = x // EDGE
    yreg = y // EDGE
    match dir, yreg, xreg:
        case L, 0, _: return 149-x, 99, R
        case L, 1, _: return  49,x+ 50, U
        case L, 2, _: return 149-x,149, R
        case L, 3, _: return 149,x-100, U
        case R, 0, _: return 149-x,  0,  L
        case R, 1, _: return 100,x- 50,  D
        case R, 2, _: return 149-x, 50,  L
        case R, 3, _: return   0,x-100,  D
        case D , _, 0: return   0,y+100,  D
        case D , _, 1: return 100+y, 49, R
        case D , _, 2: return -50+y, 99, R
        case T , _, 0: return  50+y, 50,  L
        case T , _, 1: return 100+y,  0,  L
        case T , _, 2: return 199,y-100, U       

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
                     nextY, nextX = wrapMap(board, x,y, dir)
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

def move2(board, path, printb = False):
    y = 0
    x = 0
    dir = 0
    # starting position
    while (x,y) not in board or board[(x,y)] != '.': x +=1
    print('start', x, y)
    for p in path:
        print(p)
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
                # print('n', nextX, nextY)
                # check for edges
                if (nextX, nextY) not in board:
                    #find next
                    nextX, nextY, dir = wrapCube(x,y, dir)
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
    #move(board, path)  
    # printBoard(board, maxX, maxY)
    print(board)
    move2(board, path)
