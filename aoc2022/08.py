import numpy as np

def loop1(m):
    res = np.pad(np.zeros((len(m)-2, len(m[0])-2)).astype(int), 1, 'constant', constant_values=1)

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            if res[j][i] > 0:
                continue
            l = m[j][i]
            row = m[j]
            col = m[:,i]

            left = max(row[:i])
            right = max(row[i+1:])
            top = max(col[:j])
            bottom = max(col[j+1:])

            nbrs = min([left, right, top, bottom])
            if l > nbrs:
                res[j][i] = 1  
    
    print(res.sum())
            
def loop2(m):
    res = np.zeros((len(m), len(m[0]))).astype(int)

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            tree = m[j][i]
            row = m[j]
            col = m[:,i]
            left = calcScore(row[:i], tree, True)
            right = calcScore(row[i+1:], tree, False)
            top = calcScore(col[:j], tree, True)
            bottom = calcScore(col[j+1:], tree, False)
            score = left * right * bottom * top
            res[j][i] = score
    print(res.max())

def calcScore(arr, val, reverse):
    if arr.size == 0: return 0
    if reverse: arr = arr[::-1]

    s = 0
    for v in arr:
        if v < val:
            s+=1
        else:
            s+=1
            break
    return s

with open("08.txt") as f:
    forest = np.array([list(l) for l in (x.strip() for x in f)]).astype(int)
    loop1(forest)
    loop2(forest)


