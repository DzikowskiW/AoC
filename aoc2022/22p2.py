N = -1
S = 1
W = complex(0, -1)
E = complex(0, 1)

R = pow(complex(0,1), 3)
L = pow(complex(0,1), 1)

EDGE = 50
START = complex(0, 50)

# HISTORY = set([])

def wrap(y,x, dir):
    global N, S, W, E
    ey = y // EDGE
    ex = x // EDGE
    if dir == N:
        if ex == 0: return complex(50 + x, 50), E
        elif ex == 1: return complex(100 + x, 0), E
        elif ex == 2: return complex(199, x - 100), N
    elif dir == S:
        if ex == 0: return complex(0, x + 100), S
        if ex == 1: return complex(100 + x, 49), W
        if ex == 2: return complex(x - 50, 99), W
    elif dir == E:
        if ey == 0: return complex(149 - y, 99), W 
        if ey == 1: return complex(49, 50 + y), N
        if ey == 2: return complex(149 - y, 149), W
        if ey == 3: return complex(149, y - 100), N
    elif dir == W:
        if ey == 0: return complex(149 - y, 0), E
        if ey == 1: return complex(100, y-50), S
        if ey == 2: return complex(149 - y, 50), E
        if ey == 3: return complex(0, y - 100), S
    
def walk(cube, head, val, turn):
    pos, dir = head
    # walk
    turn_val = 0
    log = False
    ndir = dir
    if dir == N: turn_val = 3
    if dir == W: turn_val = 2
    if dir == S: turn_val = 1
    print('step', int(head[0].real)+1, int(head[0].imag)+1, turn_val, val)
    for _ in range(val):
        nxt:complex = pos + dir
        ny, nx = int(nxt.real), int(nxt.imag)
        # check next coords
        if not (0 <= ny < 4*EDGE and 0 <= nx < len(cube[ny])) or (cube[ny][nx] not in ['.','#']):
            npos, ndir = wrap(ny, nx, dir)
            ny, nx = int(npos.real), int(npos.imag)
        # check next symbol on cube
        if cube[ny][nx] == '#':
            break
        elif cube[ny][nx] == '.':
            pos = complex(ny,nx)
            dir = ndir
            # HISTORY.add((int(pos.real),int(pos.imag),'X'))
        else:
            assert(False)

    #turn
    turn_val = 0
    if dir == N: turn_val = 3
    if dir == W: turn_val = 2
    if dir == S: turn_val = 1
    print('step', int(pos.real)+1, int(pos.imag)+1, turn_val, turn)
    if turn == 'L':
        dir *= L
    elif turn == 'R':
        dir *= R
    
    return (pos, dir)

def process(cube, path):
    head = (START,E)
    ipath = 0
    tmp = ''
    while ipath < len(path):
        c = path[ipath]
        if c not in ['L','R']:
            tmp += c
        else:
            if len(tmp) == 0:
                tmp = 0
            head = walk(cube, head, int(tmp), c)
            tmp = ''
        ipath += 1
    if len(tmp) > 0:
        head = walk(cube, head, int(tmp), None)
    fy, fx = int(head[0].real), int(head[0].imag)
    turn_val = 0
    if head[1] == N: turn_val = 3
    if head[1] == W: turn_val = 2
    if head[1] == S: turn_val = 1
    print(fy+1,fx+1,turn_val)
    print(1000*(fy +1) + 4* (fx + 1) + turn_val)
    # to_file(cube, HISTORY)
    return
            
def to_file(cube,history):
    f = open("output/22o.txt","w")
    out = [[*l] for l in cube]
    for y,x,c in history:
        out[y][x] = c
    for l in out:
        f.write(''.join(l))
        f.write('\n')
    f.close()

lines = open("22.txt").read().rstrip().split('\n')
path = lines.pop()
lines.pop()
path = path
process(lines, path)