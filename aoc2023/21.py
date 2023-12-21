import numpy as np
import functools

GRID = []
EDGES = [(-1, 0), (0, 1), (1, 0), (0, -1)]

@functools.cache
def stepper(y,x,steps):
    if steps == 0:
        return set([(y, x)])
    res = set()
    for dy,dx in EDGES:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < GRID.shape[0] and 0 <= nx < GRID.shape[1] and GRID[ny,nx] != '#':
                res.update(stepper(ny, nx, steps-1))
    return res

def part1():
    [sy], [sx] = np.where(GRID == 'S')
    print(len(stepper(sy,sx,64)))

with open("input/21.txt") as f:
    lines = f.read().rstrip().split('\n')
    input = [[c for c in l] for l in lines]
    GRID = np.array(input, dtype=str)
    part1()