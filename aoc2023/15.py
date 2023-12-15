from functools import reduce
from collections import defaultdict

def hash(i):
    return reduce(lambda r, c: (ord(c)+r)*17 % 256, i, 0)

with open("input/15.txt") as f:
    input = f.read().rstrip("\n")
    summ = sum([hash(i) for i in input.split(',')])
    print('part 1', summ)
    
    summ = 0
    mapp = defaultdict(list)
    for i in input.split(',') :
        if i[-1] == '-':
            itxt = i[0:-1]
            idx = hash(itxt)
            for ii, m in enumerate(mapp[idx]):
                if m[0] == itxt:
                    mapp[idx].pop(ii)
        else:
            label, val = i.split('=')
            idx = hash(label)
            changed = False
            for i,v in enumerate(mapp[idx]):
                if v[0] == label:
                    mapp[idx][i][1] = val
                    changed = True
                    break
            if not changed:
                mapp[idx].append([label, val])
        
    for i in mapp:
        for j,val in enumerate(mapp[i]):
            summ += (i + 1) * (j + 1) * int(val[1])
    print('part 2', summ)

    
