from functools import cmp_to_key

def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if (l == r):
            return 0
        elif (l < r):
            return -1
        else:
            return 1
    elif isinstance(l, list) and isinstance(r,list):
        i = 0
        minlen = min(len(l), len(r))
        while i < minlen:
            cmpres = compare(l[i],r[i])
            i+=1
            if cmpres != 0:
                return cmpres
        if len(l) == len(r):
            return 0
        elif len(l) == minlen:
            return -1
        else:
            return 1
    elif isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])
    elif isinstance(l, int) and isinstance(r, list):
        return compare([l], r)
    else:
        assert(False)
        
def part1(input):
    vals = []
    rightOrders = 0
    n = 0
    for i in input: 
        if i == '':
            n += 1
            if compare(*vals) == -1:
                rightOrders += n
            assert(len(vals) == 2)
            vals = []
        else:
            vals.append(eval(i))
    if compare(*vals) == -1:
        rightOrders += n+1
        
    print('part 1', rightOrders)
    
def part2(input):
    vals = [[[2]], [[6]]]
    
    for i in input: 
        if i != '':
            vals.append(eval(i))
    
    vals = sorted(vals, key=cmp_to_key(compare))
    print('part 2', (vals.index([[2]]) + 1) * (vals.index([[6]]) + 1))

with open("aoc2022/13.txt") as f:
    input = [x.strip() for x in f]
    
    part1(input)
    part2(input)
