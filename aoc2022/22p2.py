import re

N = -1
S = 1
W = complex(0, -1)
E = complex(0, 1)

R = pow(complex(0,1), 3)
L = pow(complex(0,1), 1)

EDGE = 50
START = complex(5, 60)

HISTORY = set([])

def wrap(y,x, dir):
    global N, S, W, E
    print(dir, y//EDGE, x//EDGE)
    match (dir, y//EDGE, x//EDGE):
        case (N, _, 0): print('N0');return complex(50 + x, 50), E
        case (N, _, 1): print('N1');return complex(100 + x, 0), E
        case (N, _, 2): print('N2');return complex(149, x - 100), N
        case (S, _, 0): print('S0'); return complex(0, x + 100), S
        case (S, _, 1): print('S1'); return complex(150 + x, 49), W
        case (S, _, 2): print('S2'); return complex(x - 50, 99), W
        case (E, 0, _): return complex(149 - y, 99), W 
        case (E, 1, _): return complex(y + 50, 49), N
        case (E, 2, _): return complex(149 - y, 149), W
        case (E, 3, _): return complex(149, y - 100), N
        case (W, 0, _): return complex(149 - y, 0), E
        case (W, 1, _): return complex(100, y-50), S
        case (W, 2, _): return complex(149 - y, 50), E
        case (W, 3, _): return complex(0, y- 50), S

    assert(False)
    
def test():
    assert(wrap())
def walk(cube, head, val, turn):
    pos, dir = head
    # walk
    for _ in range(val):
        nxt:complex = pos + dir
        ny, nx = int(nxt.real), int(nxt.imag)
        # check next coords
        if not (0 <= ny < 4*EDGE and 0 <= nx < len(cube[ny])) or (cube[ny][nx] not in ['.','#']):
            print('PPPPPP', ny, nx, dir)
            npos, dir = wrap(ny, nx, dir)
            ny, nx = int(npos.real), int(npos.imag)
            print('U', ny, nx, dir)

        # check next symbol on cube
        if cube[ny][nx] == '#':
            pos = complex(ny,nx)
            # break
        elif cube[ny][nx] == '.':
            pos = complex(ny,nx)
        else:
            assert(False)
        HISTORY.add((int(pos.real),int(pos.imag),'X'))

    #turn
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
    to_file(cube, HISTORY)
    return
            
def to_file(cube,history):
    f = open("output/22o.txt","w")
    out = [[*l] for l in cube]
    for y,x,c in history:
        # print(y,x,c)
        out[y][x] = c
    for l in out:
        f.write(''.join(l))
        f.write('\n')
    f.close()

lines = open("22.txt").read().rstrip().split('\n')
path = lines.pop()
lines.pop()
path = '198'
path = path
process(lines, path)