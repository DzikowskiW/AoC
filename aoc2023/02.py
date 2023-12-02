import aoc
import re

#first part
def loop1(lines):
    cubes = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    summ = 0
    for l in lines:
        game = re.search(r'^Game (\d+): (.*)$', l)
        games = game[2].split(';')
        valid = True
        for g in games:
            marbles = g.split(',')
            for m in marbles:
                marble = re.search(r'(\d+) (red|green|blue)', m)
                n = int(marble[1])
                color = marble[2]
                if (cubes[color] < n):
                    valid = False
                    break
            if not valid:
                break
        if valid:
            summ += int(game[1])
    print('part 1:', summ)
    
#second part
def loop2(lines):    
    summ = 0
    for l in lines:
        cubes = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        game = re.search(r'^Game (\d+): (.*)$', l)
        games = game[2].split(';')
        for g in games:
            marbles = g.split(',')
            for m in marbles:
                marble = re.search(r'(\d+) (red|green|blue)', m)
                n = int(marble[1])
                color = marble[2]
                cubes[color] = max(cubes[color], n)
                # print(n, color, 'cubes:', cubes[color])
        cc= cubes['red']*cubes['green']*cubes['blue']
        summ += cc
            
    print('part 2:', summ)
    
lines = aoc.input_as_lines("02.txt")
loop1(lines)
loop2(lines)