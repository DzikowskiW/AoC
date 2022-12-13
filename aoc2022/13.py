

def compare(l, r):
    #print('compare', l, ' vs ', r)
    if isinstance(l, int) and isinstance(r, int):
        assert(False)
    elif isinstance(l, list) and isinstance(r,list):
        i = 0
        minlen = min(len(l), len(r))
        while i < minlen:
            ll = l[i]
            rr = r[i]
            i+=1
            if isinstance(ll, int) and isinstance(rr, int):
                #print('compare', ll, ' vs ', rr)
                if (ll == rr):
                    continue
                elif (ll < rr):
                    return True
                else:
                    return False
            if not compare(ll,rr):
                return False
        if len(l) == i:
            return True
        return False
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
    return res

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