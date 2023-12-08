import aoc
import re
from collections import defaultdict


def loop(steps, lines):
    count = 0
    step = 0
    m = defaultdict()
    node = 'AAA'
    print(steps, lines)
    for i, l in enumerate(lines):
        a, b = l.split(" = ")
        l, r = b[1:-1].split(", ")
        m[a] = {'L':l,'R':r}

    while node != 'ZZZ':
        count += 1
        node = m[node][steps[step]]
        step = (step+1) % len(steps)
    print(count)
                

lines = aoc.input_as_lines("input/08.txt")
lines
#part 1
print('part 1:')
loop(lines[0], lines[2:])
