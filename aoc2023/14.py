import numpy as np

def loop(lines):
    # print(lines)
    llen=len(lines[0])
    for i in range(1,len(lines)):
        for j in range(1, len(lines)):
            for k in range(llen):
                if lines[j-1][k] == '.' and lines[j][k] == 'O':
                    lines[j-1][k] = 'O'
                    lines[j][k] = '.'
    # print('-----')                
    # print(lines)
    w = 0
    for i in range(len(lines)):
        for j in range(llen):
            if lines[i][j] == 'O':
                w += len(lines) - i
    print(w)

with open("input/14.txt") as f:
    input = f.read().rstrip("\n").split("\n\n")
    input = [[[*l] for l in ll.split("\n")] for ll in input]
    input = [np.array(s) for s in input]
    loop(input[0])
    
