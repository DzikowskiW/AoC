from itertools import combinations

def part1(lines):
    size = 0
    for ll in lines:
        sides = combinations(ll, 2)
        areas = tuple(map(lambda s: s[0]*s[1], sides))
        min_area = min(areas)
        size += sum(areas)*2 + min_area
    print('part 1:', size)

def part2(lines):
    size = 0
    for ll in lines:
        bow = ll[0]*ll[1]*ll[2]
        sides = sorted(ll)
        sides.pop()
        ribbon = sum(sides) * 2
        size += ribbon + bow
    print('part 2:', size)

lines = open("input/02.txt").read().rstrip().split('\n')
lines = [tuple(map(int, dim)) for dim in (ll.split('x') for ll in lines)]    
part1(lines)
part2(lines)