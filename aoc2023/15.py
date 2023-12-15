from functools import reduce

with open("input/15.txt") as f:
    input = f.read().rstrip("\n")
    summ = sum([reduce(lambda r, c: (ord(c)+r)*17 % 256, i, 0) for i in input.split(',')])
    print('part 1', summ)
