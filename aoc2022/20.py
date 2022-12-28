# OG val:num -> og_index <----> curr_index <- val:og_index CURR
import copy

def part1(og, curr):
    for i,n in enumerate(og):
        curr_i = curr.index(i)
        curr.pop(curr_i)
        index = (curr_i+n) % len(curr)
        curr.insert(index, i)
    print('part 1', calcGrove(og, curr))
    
def part2(og, curr):
    key = 811589153
    og = [n*key for n in og]
    for _ in range(0,10):    
        for i,n in enumerate(og):
            curr_i = curr.index(i)
            curr.pop(curr_i)
            index = (curr_i+n) % len(curr)
            curr.insert(index, i)
        # print('AFTER MIXING ', ii+1)
        # print([og[x] for x in curr])
    print('part 2', calcGrove(og, curr))

def calcGrove(og, curr):
    index0 = curr.index(og.index(0))
    v1000= og[curr[(index0 + 1000) % len(curr)]]
    v2000= og[curr[(index0 + 2000) % len(curr)]]
    v3000= og[curr[(index0 + 3000) % len(curr)]]
    # print(index0, v1000, v2000, v3000)
    return v1000 + v2000 + v3000

with open("aoc2022/20.txt") as f:
    lines = [x.strip() for x in f]
    og = []
    
    for l in lines:
        og.append(int(l))
    curr = [i for i in range(0, len(og))]    

    part1(copy.deepcopy(og), copy.deepcopy(curr))
    part2(copy.deepcopy(og), copy.deepcopy(curr))
    
    
