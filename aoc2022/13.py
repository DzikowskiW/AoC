

def compare(l, r):
    #print('compare', l, ' vs ', r)
    if isinstance(l, int) and isinstance(r, int):
        if (l == r):
            return 0
        elif (l < r):
            return 1
        else:
            return -1
    elif isinstance(l, list) and isinstance(r,list):
        i = 0
        minlen = min(len(l), len(r))
        while i < minlen:
            ll = l[i]
            rr = r[i]
            i+=1
            cmpres = compare(ll,rr)
            if cmpres != 0:
                return cmpres
        if len(l) == len(r):
            return 0
        elif len(l) == minlen:
            return 1
        else:
            return -1
    elif isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])
    elif isinstance(l, int) and isinstance(r, list):
        return compare([l], r)
    else:
        assert(False)

def firstCompare(l,r):
    print('\n\ncompare ')
    print(l, '\n', r, '\n' )
    res = compare(l, r)
    print(res)
    return res == 1

with open("aoc2022/13.txt") as f:
    input = [x.strip() for x in f]
    
    vals = []
    rightOrders = []
    n = 0
    for i in input: 
        if i == '':
            n += 1
            if firstCompare(*vals):
                rightOrders.append(n)
            assert(len(vals) == 2)
            vals = []
        else:
            vals.append(eval(i))
    n += 1
    if firstCompare(*vals):
        rightOrders.append(n)
    print(rightOrders)
    print('right', sum(rightOrders))
    #print(input)