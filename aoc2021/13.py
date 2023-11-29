import numpy as np

def fold(m, fold):
    print('fold', fold)
    twice = 0
    (axis, val) = fold
    if (axis == 'y'): 
        i = 0
        lenY = len(m)-1
        while  val-i >=0 and val+i < len(m):
            print(val-i, val+i)
            m[val-i] = np.add(m[val-i],m[val+i])
            i+=1
        m = m[:val, :]
    if (axis == 'x'):
        i = 0
        lenX = len(m[0])-1
        while  val-i >=0 and val+i < len(m[0]):
            for k in range(len(m)):
                if (m[k][val-i] == 0):
                    m[k][val-i] += m[k][val+i]
                    twice += m[k][val+i]
            i+=1
        m = m[:, :val]
    return m

def p1(data, folds):
    #initial matrix
    maxX = max(map(lambda val: val['x'], data))
    maxY = max(map(lambda val: val['y'], data))
    m = np.zeros((maxY+1, maxX+1), dtype=np.int8)    
    for d in data:
        m[d['y']][d['x']] = 1
    
    m = fold(m, folds[0])
    return sum(map(lambda v: 1 if v > 0 else 0, m.flatten()))

def p2(data):
    #initial matrix
    maxX = max(map(lambda val: val['x'], data))
    maxY = max(map(lambda val: val['y'], data))
    m = np.zeros((maxY+1, maxX+1), dtype=np.int8)    
    for d in data:
        m[d['y']][d['x']] = 1
    
    #fold
    for f in folds:
        m = fold(m, f)
        print('lx', len(m[0]))
        print('ly', len(m))
    
    #print
    for y in m:
        s = ''
        for x in y:
            s+= '#' if x > 0 else '.'
        print(s)
    return 'done'

            
with open("13.txt") as f:
    lines = [x.strip() for x in f]
    data = []
    isFolding = False
    folds = []
    for line in lines:
        if len(line) == 0:
            isFolding = True
            continue
        if not isFolding:
            [x, y] = line.split(',')
            data.append({ 'x': int(x), 'y': int(y)})
        else:
            [txt, val] = line.split('=') 
            folds.append((txt[-1], int(val)))
    
    print('Part 1: \n', p1(data, folds)) 
    print('Part 2: \n', p2(data)) 
