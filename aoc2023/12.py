import aoc
import functools

@functools.cache
def calc(springs, clusters):
    if not clusters:
        if '#' not in springs:
            return 1
        else:
            return 0
    if not springs:
        return 0
    if len(springs) < clusters[0]:
        return 0
    
    nc = clusters[0]
    res = 0
    if springs[0] in ['.', '?']:
        res += calc(springs[1:], clusters)
    if springs[0] in ['#', '?']:
        if '.' in springs[0:nc]:
            pass
        elif nc == len(springs):
            if len(clusters) == 1:
                res += 1
        elif springs[nc] in ['?','.']:
            res += calc('.'+springs[nc+1:], clusters[1:])
    return res

def loop(lines):
    part1 = 0
    part2 = 0
    for l in lines:
        springs, conditions = l.split(' ')
        part1 += calc(springs, tuple(map(int,conditions.split(','))))
        springs = ((springs + '?') * 5)[0:-1]
        conditions = ((conditions + ',') * 5)[0:-1]
        part2 += calc(springs, tuple(map(int,conditions.split(','))))
    print('part1:', part1) 
    print('part2:', part2) 
    

lines = aoc.input_as_lines("input/12.txt")
loop(lines)
