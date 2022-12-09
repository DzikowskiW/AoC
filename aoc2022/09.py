import numpy as np
import math

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return '('+str(self.x)+','+str(self.y)+')'

def printRope(h,t):
    matrix = np.full((6,6),' ', dtype=str)
    
    matrix[0,0] = 's'
    matrix[t.y, t.x] = 'T' 
    matrix[h.y, h.x] = 'H'

    print(np.flipud(matrix))

def printLongRope(rope):
    matrix = np.full((6,6),' ', dtype=str)
    matrix[0,0] = 's'
    revrope = rope[::-1]
    for r in range(len(revrope)):
        point = revrope[r]
        c = r
        if r == 0: c = 'T'
        if r == len(revrope)-1: c = 'H'
        matrix[point.y, point.x] = c 
    print(np.flipud(matrix))

def moveTail(h,t):
    dx = math.floor((h.x-t.x)/2) 
    dy = math.floor((h.y-t.y)/2) 
    dt = math.sqrt(pow(h.x-t.x,2) + pow(h.y - t.y,2))
    if dt < 1.5:
        return
    if dx == 0 and dt > 2.1:
        dx += math.floor(h.x-t.x)
    if dy == 0 and dt > 2.1:
        dy += math.floor(h.y-t.y)
    t.x += dx
    t.y += dy

def moveRope(h,t,move, visited):
    dir = move[0]
    for i in range(0, move[1]):
        if dir == 'U':
            h.y += 1
        elif dir == 'D':
            h.y -= 1
        elif dir == 'L':
            h.x -= 1
        elif dir == 'R':
            h.x += 1
        else: 
            assert(False)
        moveTail(h,t)
        visited[t.x, t.y] = 1 

def moveLongRope(rope,move, visited):
    dir = move[0]
    for i in range(0, move[1]):
        h = rope[0]
        if dir == 'U':
            h.y += 1
        elif dir == 'D':
            h.y -= 1
        elif dir == 'L':
            h.x -= 1
        elif dir == 'R':
            h.x += 1
        else: 
            assert(False)
        
        for ri in range(1,len(rope)):
            h = rope[ri-1]
            t = rope[ri]
            moveTail(h,t)
            if (ri == len(rope)-1):
                visited[t.x, t.y] = 1 

def loop1(moves):
    visited = np.zeros((6000,6000), dtype=int)
    visited[0,0] = 1
    h = Point(0,0)
    t = Point(0,0)
    longRope = [Point(0,0) for i in range(0,10)]

    for m in moves:
        #part 1
        #moveRope(h, t, m, visited)

        #part 2
        moveLongRope(longRope, m, visited)
    
    print('result', visited.sum())
    return
            
with open("09.txt") as f:
    input = [p.split(' ') for p in [x.strip() for x in f]]
    for i in input:
        i[1] = int(i[1])

    loop1(input)


