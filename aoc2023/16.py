W = (0,-1)
E =  (0,1)
N = (-1,0)
S = (1,0)

IDXS = {
    W: 0,
    E: 1,
    N: 2,
    S: 3
}

def part2(cave):
    starts = []
    vlen = len(cave)
    hlen = len(cave[0])
    res = 0
    for i in range(vlen):
        starts.append((i,0, E))
        starts.append((i, hlen-1, W))
    for j in range(hlen):
        starts.append((0, j, S))
        starts.append((vlen-1, j, N))
    for s in starts:
        res = max(res, raytrace(cave, s))
    return res

def part1(cave):
    return raytrace(cave, (0,0,E))

def raytrace(cave, start):
    vlen = len(cave)
    hlen = len(cave[0])
    energized  = set()
    visited =set()
    toVisit = [start]
    while toVisit:
        y,x,dir = toVisit.pop()
        if y < 0 or y >= vlen:
            continue
        if x < 0 or x >= hlen:
            continue
        if (y,x,dir) in visited:
            continue
        visited.add((y,x,dir))
        energized.add((y,x))
        c = cave[y][x]
        changeDir = None
        if c == '.':
            changeDir = ([W], [E], [N], [S])
        elif c == '/':
            changeDir = ([S], [N], [E], [W])
        elif c == '\\':
            changeDir = ([N], [S], [W], [E])
        elif c == '|':
            changeDir = ([N,S], [N,S], [N], [S])
        elif c == '-':
            changeDir = ([W], [E], [W,E], [W,E])
        for next_dir in changeDir[IDXS[dir]]:
            toVisit.append((y + next_dir[0], x + next_dir[1], next_dir))
    return len(energized)

with open("input/16.txt") as f:
    cave = f.read().rstrip().split('\n')
    print('part 1', part1(cave))
    print('part 2', part2(cave))
    

    
