import aoc
import re

def loop(lines):
    summ = 0   
    for line in lines:
        winners, numbers = line.split(': ')[1].split(' | ')
        winners = winners.split(' ')
        numbers = numbers.split(' ')
        score = 0
        for n in numbers:
            if len(n) > 0 and n in winners:
                if score == 0: score = 1
                else: score *= 2
        summ += score
        print(numbers)
        print(winners)
        print(score)
    print(summ)
        

lines = aoc.input_as_lines("input/04.txt")
loop(lines)

