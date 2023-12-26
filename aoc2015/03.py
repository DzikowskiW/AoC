def part1(line):
    houses = set()
    y,x = 0,0
    houses.add((y,x))
    cmap = { '>': (0,1), '<': (0,-1), 'v': (1,0), '^': (-1, 0)}
    for c in line:
        y = y + cmap[c][0]
        x = x + cmap[c][1]
        houses.add((y,x))
    print('part 1', len(houses))

line = open("input/03.txt").read().rstrip().split('\n')[0]
part1(line)