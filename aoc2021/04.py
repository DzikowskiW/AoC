import operator
import numpy as np
from collections import defaultdict


def loopP1(draws, bingos, checks):
    for draw in draws:
        for i, bingo in enumerate(bingos):
            check = checks[i]
            if writeBingo(draw, bingo, check):
                #winner
                sum = 0
                for k in range(len(bingo)):
                    for l in range(len(bingo[k])):
                        if check[k][l] == 0: 
                            sum += bingo[k][l]
                # print('END ', draw, sum, draw * sum)
                return i

def loopP2(draws, bingos, checks):
    unsolved = range(len(bingos))
    for draw in draws:
        for i, bingo in enumerate(bingos):
            if not i in unsolved:
                continue
            check = checks[i]
            if writeBingo(draw, bingo, check):
                unsolved.remove(i)
                if (len(unsolved) == 0):
                    #winner
                    sum = 0
                    for k in range(len(bingo)):
                        for l in range(len(bingo[k])):
                            if check[k][l] == 0: 
                                sum += bingo[k][l]
                    print('END P2', draw, sum, draw * sum)
                    return

def checkBingo(num, check, i, j):
    row = 0
    col = 0
    for x in range(len(check)):
        row += check[i][x]
        col += check[x][j]
    


def writeBingo(num, bingo, check):
    binlen = len(bingo)
    for i in range(len(bingo)):
        for j in range(len(bingo[i])):
            if num == bingo[i][j]:
                check[i][j] = 1
                #check rows
                rowChecks = 0
                for k in range(len(check[i])):
                    rowChecks += check[i][k]
                
                if (rowChecks == len(check[i])):
                    print('WINNER ROW')
                    return True

                #check cols
                colChecks = 0
                for k in range(len(check[i])):
                    colChecks += check[k][j]
                
                if (colChecks == len(check[i])):
                    print('WINNER COL')
                    return True
    return False

with open("04.txt") as f:
    lines = [x.strip() for x in f]
    draws = lines.pop(0).split(',');
    draws = map(lambda d: int(d), draws)
    lines.pop(0)

    bingos = []
    checks = []

    bingo = []
    check = []
    for line in lines:
        if line == '':
            bingos.append(bingo)
            checks.append(check)
            check = []
            bingo = []
        else:
            bingo.append(map(lambda val : int(val), line.split()))
            check.append(map(lambda val : 0, line.split()))
    
    bingos.append(bingo)
    checks.append(check)

    #loop
    loopP2(draws, bingos, checks)

    # for check in checks:
    #     print(np.matrix(check))
    #     print("------")


    # for bingo in bingos:
    #     print(np.matrix(bingo))
    #     print("------")
