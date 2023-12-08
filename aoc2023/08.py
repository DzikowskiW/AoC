import aoc
import re
import math
from collections import defaultdict

def part2(steps, lines):
    count = 0
    current_step = 0
    m = defaultdict()
    nodes = []
    node_counter = defaultdict(int)
    
    #parse input
    for line in lines:
        a, b = line.split(" = ")
        l, r = b[1:-1].split(", ")
        m[a] = {'L':l,'R':r}
        if a[2] == 'A':
            nodes.append(a)
    
    #find step counter for each node
    for ii, node in enumerate(nodes):
        while node[2] != 'Z':
            node_counter[ii]  += 1
            node = m[node][steps[current_step]]
            current_step = (current_step + 1) % len(steps)

    #lowest common multiplier
    count = math.lcm(*list(node_counter.values()))
    print(count)


def part1(steps, lines):
    count = 0
    current_step = 0
    m = defaultdict()
    current_node = 'AAA'
    for line in lines:
        a, b = line.split(" = ")
        l, r = b[1:-1].split(", ")
        m[a] = {'L':l,'R':r}

    while current_node != 'ZZZ':
        count += 1
        current_node = m[current_node][steps[current_step]]
        current_step = (current_step + 1) % len(steps)
    print(count)
                

lines = aoc.input_as_lines("input/08.txt")

#part 1
print('part 1:')
part1(lines[0], lines[2:])

#part 1
print('part 2:')
part2(lines[0], lines[2:])
