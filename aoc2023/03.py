import aoc
import math
import numpy as np

#return full number with its start coords 
def get_full_number(engine, row, col):
    numm = str(engine[row][col])
    cl = col - 1
    while engine[row][cl].isdigit():
        numm = str(engine[row][cl]) + numm
        cl -= 1
    cr = col + 1
    while engine[row][cr].isdigit():
        numm += engine[row][cr]
        cr += 1
    return (int(numm), row, cl)

# returns numbers surrounding (row,col) point
def find_part_numbers(engine, row, col):
    unique_numbers = set()
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if engine[r][c].isdigit():
                full_number = get_full_number(engine, r, c)
                unique_numbers.add(full_number)
    return list(map(lambda n: n[0], unique_numbers))
    
def loop(lines):
    lines = list(map(lambda l: [ *l], lines))
    engine = np.pad(lines,1, constant_values='.')
    part1 = 0
    part2 = 0
    for row in range(engine.shape[0]):
        for col in range(engine.shape[1]):
            #part 1
            if engine[row][col] != '.' and not engine[row][col].isdigit():
                part1 += sum(find_part_numbers(engine, row, col))
            #part 2
            if engine[row][col] == '*':
                nums = find_part_numbers(engine, row, col)
                if len(nums) == 2:
                    part2 += math.prod(nums)
    print('part 1:', part1)
    print('part 2:', part2)

lines = aoc.input_as_lines("input/03.txt")
loop(lines)

