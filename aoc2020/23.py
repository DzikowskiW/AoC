import operator
from collections import defaultdict

with open("23.txt") as f:
    lines = [x.strip() for x in f]

DIR = {
    "e": (1, -1, 0),
    "se": (0, -1, 1),
    "sw": (-1, 0, 1),
    "w": (-1, 1, 0),
    "nw": (0, 1, -1),
    "ne": (1, 0, -1),
}


def toggle(set_, value):
    if value in set_:
        set_.discard(value)
    else:
        set_.add(value)


seen = set()
for line in lines:
    pos = (0, 0, 0)
    move = ""
    for c in line:
        move += c
        if move in DIR:
            pos = tuple(map(operator.add, pos, DIR[move]))
            move = ""
    toggle(seen, pos)

old_tiles = seen.copy()
new_tiles = set()
white_tiles_with_black_neighbours = defaultdict(int)
for _ in range(100):
    for tile in old_tiles:
        neighbours = [tuple(map(operator.add, tile, move)) for move in DIR.values()]
        black_neighbours = 0
        for neighbour in neighbours:
            if neighbour in old_tiles:
                black_neighbours += 1
            else:
                white_tiles_with_black_neighbours[neighbour] += 1
        if black_neighbours == 0 or black_neighbours > 2:
            continue
        else:
            new_tiles.add(tile)
    for tile, black_neighbours in white_tiles_with_black_neighbours.items():
        if black_neighbours == 2:
            new_tiles.add(tile)
    old_tiles = new_tiles.copy()
    new_tiles = set()
    white_tiles_with_black_neighbours = defaultdict(int)

print("Part 1:", len(seen))
print("Part 2:", len(old_tiles))