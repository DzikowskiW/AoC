import numpy as np

def findAxis(shape, smudges = 0):
    for i in range(1, len(shape)):
        size = min(i, len(shape)-i)
        if size > 0:
            arr1 = shape[i-size:i]
            arr2 = shape[i:i+size]
            arr_diff_count = np.count_nonzero(np.logical_not(arr1 == np.flipud(arr2)).astype(int))
        if arr_diff_count == smudges:
            return i
    return 0
        
def summarize(shapes, smudges):
    summ = 0
    for s in shapes:
        summ += findAxis(s, smudges)*100
        summ += findAxis(s.T, smudges)
    return summ
    
with open("input/13.txt") as f:
    input = f.read().rstrip("\n").split("\n\n")
    input = [[[*l] for l in ll.split("\n")] for ll in input]
    shapes = [np.array(s) for s in input]
    print('part 1:', summarize(shapes, 0))
    print('part 2:', summarize(shapes, 1))
