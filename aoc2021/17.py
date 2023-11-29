import numpy as np
import re

def isValid(x,y, start, end):
    sx = x
    sy = y
    vX = x
    vY = y
    while True:

        if x  <= 0 and x < start['x']: return False
        if x > end['x']: return False
        if y < start['y']: return False
        if x >= start['x'] and x <= end['x'] and y >= start['y'] and y <= end['y']:
            return (sx, sy)
        vX = vX-1 if vX > 0 else 0
        vY = vY-1
        x += vX
        y += vY


def p2(start, end):
    points = []
    print(start, end)
    for i in range(end['x']+1):
        for j in range(abs(start['y'])+1):
            v1 = isValid(i, j, start, end)
            v2 = isValid(i, -j, start, end)
            if v1 is not False:
                points.append(v1) 
            if j != -j and v2 is not False:
                points.append(v2)
    return len(set(points))



def p1(start, end):
    #calc max Y
    return sum( range(0, min(start['y'], end['y']), -1) )

with open("17.txt") as f:
    lines = [x.strip() for x in f]
    transmission = ''
    startX = 0
    endX = 0
    startY = 0
    endY = 0

    for line in lines:
        r = re.search('target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)$', line)
        startX = int(r.group(1))
        endX = int(r.group(2))
        startY = int(r.group(3))
        endY = int(r.group(4))

    #print('P1', p1({ 'x': startX, 'y': startY }, { 'x': endX, 'y': endY}))
    print('P2', p2({ 'x': startX, 'y': startY }, { 'x': endX, 'y': endY}))