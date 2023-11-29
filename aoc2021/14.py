from more_itertools import interleave_longest, windowed
from collections import Counter

def expand(c1, c2, minC, maxC, assgn, depth):
    if depth == 0: 
        return 0
    if depth > 35:
        print('depth', c1, c2, depth)
    newC = assgn[c1 + c2]
    sum = 0
    if newC == maxC: sum +=1
    if newC == minC: sum -=1
    return sum + expand(c1, newC, minC, maxC, assgn, depth-1) + expand(newC, c2, minC, maxC, assgn, depth-1)

def p1(startTxt, assgn, steps):
    txt = startTxt

    #count min max
    count = dict()
    for c in txt:
        if not c in count:
            count[c] = 0
        count[c] += 1
    maxC = 0
    minC = 0
    print(count)
    for k in count.keys():
        if maxC == 0:
            maxC = k
            minC = k
        else:
            maxC = k if count[k] > count[maxC] else maxC
            minC = k if count[k] < count[minC] else minC

    print('max', maxC, 'min', minC)    
    return count[maxC] - count[minC]

def expand2(pairCount, letterCount, assgn):
    #for each rule count how many new will be made
    newPairCount = pairCount.copy()
    for pairKey in pairCount:
        c0 = pairKey[0]
        c1 = pairKey[1]
        letter = assgn[c0 + c1]
        newPair1 = c0 + letter
        newPair2 = letter + c1
        newPairCount[newPair1] += pairCount[pairKey]
        newPairCount[newPair2] += pairCount[pairKey]
        newPairCount[pairKey] -= pairCount[pairKey]
        letterCount[letter] += pairCount[pairKey]
    
    return newPairCount, letterCount

    
    return 0
def p2(startTxt, assgn, steps):
    txt = list(startTxt)
    pairs = windowed(txt, 2)
    pairCount = Counter(dict.fromkeys(assgn.keys(), 0))
    letterCount = Counter(startTxt)
    
    #initial count
    for pair in pairs:
        pairCount[pair[0]+pair[1]] += 1
    print(pairCount.items())

    print(letterCount)

    #each step
    for i in range(steps):
        pairCount, letterCount = expand2(pairCount, letterCount, assgn)
        print(letterCount)
    return max(letterCount.values()) - min(letterCount.values())
 


with open("14.txt") as f:
    lines = [x.strip() for x in f]
    startTxt = ''
    assgn = dict()
    for line in lines:
        if len(startTxt) == 0:
            startTxt = line
        elif len(line) == 0:
            continue
        else:
            assgn[line[0]+line[1]] = line[-1]
    
    #print('P1', p1(startTxt, assgn, 10))    
    print('P2', p2(startTxt, assgn, 40))