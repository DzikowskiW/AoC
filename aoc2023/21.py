import numpy as np
import functools
from collections import defaultdict

GRID = []
EDGES = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# working but slooow
@functools.cache
def stepper(y,x,steps):
    if steps == 0:
        return set([(y, x)])
    res = set()
    for dy,dx in EDGES:
            ny = dy + y
            nx = dx + x
            cy = ny % GRID.shape[1]
            cx = nx % GRID.shape[0]
            if GRID[cy,cx] != '#':
                res.update(stepper(ny, nx, steps-1))
    return res

# faster
def bfs_stepper(sy, sx, steps):
    leny = len(GRID)
    lenx = len(GRID[0])
    seen = set()
    possible = set()
    next = [(sy,sx,steps)]
    while next:
        y,x,s = next.pop(0)
        if s % 2 == 0:
            possible.add((y,x))
        if s == 0:
            continue
        for dy,dx in EDGES:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < leny and 0 <= nx < lenx and GRID[ny,nx] != '#' and (ny,nx) not in seen:
                seen.add((ny,nx))
                next.append((ny,nx, s - 1)) 
    return len(possible)
              

def part1():
    [sy], [sx] = np.where(GRID == 'S')
    res = bfs_stepper(sy, sx, 64)
    print('Part 1', res)
    
def part2(steps = 26501365):
    size = len(GRID)
    [sy], [sx] = np.where(GRID == 'S')
    assert sy == sx == size // 2
    assert steps % size == size // 2
    
    #number of grids
    grid_width = steps // size - 1
    
    # number of full odd and even grids
    odd = (grid_width // 2 * 2 + 1) ** 2
    even = ((grid_width + 1) // 2 * 2) ** 2
    
    # steps in full grids
    odd_points = bfs_stepper(sy, sx, size * 2 + 1)
    even_points = bfs_stepper(sy, sx, size * 2)
    
    # steps on corners
    corners = defaultdict(int)
    corners['top'] = bfs_stepper(size - 1, sx, size - 1)
    corners['left'] = bfs_stepper(sy, size -1, size - 1)
    corners['right'] = bfs_stepper(sy, 0, size - 1)
    corners['bottom'] = bfs_stepper(0, sx, size - 1)
    
    # steps on edges
    edges_small = defaultdict(int)
    edges = defaultdict(int)
    edges_small['top_left'] = bfs_stepper(size - 1, size - 1, size // 2 - 1)
    edges_small['top_right'] = bfs_stepper(size - 1, 0, size // 2 - 1)
    edges_small['bottom_left'] = bfs_stepper(0, size - 1, size // 2 - 1)
    edges_small['bottom_right'] = bfs_stepper(0, 0, size // 2 - 1)
    edges['top_left'] = bfs_stepper(size - 1, size - 1, size * 3 // 2 - 1)
    edges['top_right'] = bfs_stepper(size - 1, 0, size * 3 // 2 - 1)
    edges['bottom_left'] = bfs_stepper(0, size - 1, size * 3 // 2 - 1)
    edges['bottom_right'] = bfs_stepper(0, 0, size * 3 // 2 - 1)
    
    res = odd_points * odd + even_points * even 
    res += sum(corners.values()) 
    res += sum(edges_small.values()) * (grid_width + 1) + sum(edges.values()) * grid_width
    print('part 2', res)
        
with open("input/21.txt") as f:
    lines = f.read().rstrip().split('\n')
    input = [[c for c in l] for l in lines]
    GRID = np.array(input, dtype=str)
    part1()
    part2()