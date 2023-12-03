import aoc
import re
import numpy as np

def getNumber(engine, x,y, stopy=-1):
    numm = str(engine[x][y])
    yl = y-1
    while engine[x][yl].isdigit():
        if yl < 0: 
            break
        numm = str(engine[x][yl]) + numm
        yl -= 1

    yr = y+1
    if yr < engine.shape[0]:
        while engine[x][yr].isdigit():
            if yr >= engine.shape[0]:
                break
            numm += engine[x][yr]
            yr += 1
    # print((numm, yl+1,yr-1))
    return (int(numm), yl+1,yr-1)

def findPartNumbers(engine, x, y):
    nums = set()
    for xx in range(x-1, x+2):
        if xx < 0 or xx >= engine.shape[0]:
                break
        for yy in range(y-1, y+2):
            if (engine[xx][yy].isdigit()):
                numm = getNumber(engine, xx, yy)
                nums.add(numm)
    return nums      

#first part
def loop1(lines):
    print('part 1')
    lines1 = list(map(lambda l: ['.', *l, '.'], lines))
    
    engine = np.array(lines1)
    print(engine.shape)
    print(engine)
    summ = 0
    nums = set()
    for x in range(engine.shape[0]):
        for y in range(engine.shape[1]):
            if engine[x][y] != '.' and not engine[x][y].isdigit():
                numm = findPartNumbers(engine, x, y)
                print('num', engine[x][y], x, y, numm)
                nums = nums.union(numm)
    print(nums)
    for nn in nums:
        summ += nn[0]
    print(summ)
    
    
    
    
    
#second part
def loop2(lines):    
    print('part 2')
    # print('part 2:', summ)
    
lines = aoc.input_as_lines("input/03.txt")
loop1(lines)
#loop2(lines)