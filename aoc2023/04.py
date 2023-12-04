import aoc
import functools
from collections import defaultdict

def process_next_cards(lines, number):
    score = 0
    winners, numbers = lines[number].split(': ')[1].split(' | ')
    winners = [ int(w) for w in winners.split(' ') if len(w) > 0 ]
    numbers = [ int(n) for n in numbers.split(' ') if len(n) > 0 ]
    for n in numbers:
        if n in winners:
            score +=1
    return list(range(number + 1, number + score + 1))

score_cache = dict()
def count_score(index, cards):
    if index not in score_cache: 
        score = 1
        for c in cards[index]:
            score += count_score(c, cards)
        score_cache[index] = score
    return score_cache[index]

def loop2(lines):
    counter = 0
    cards = defaultdict(list)
    for i in range(len(lines)):
        cards[i] = process_next_cards(lines, i)
    for i in range(len(cards)):
        counter += count_score(i, cards)
    print('part 2:', counter)
    
def loop1(lines):
    points = defaultdict(int)  
    for i, line in enumerate(lines):
        winners, numbers = line.split(': ')[1].split(' | ')
        winners = [ int(w) for w in winners.split(' ') if len(w) > 0 ]
        numbers = [ int(n) for n in numbers.split(' ') if len(n) > 0 ]
        for n in numbers:
            if n in winners:
                if i not in points: 
                    points[i] = 1
                else: 
                    points[i] *= 2
    print('part 1:', sum(points.values()))
        
lines = aoc.input_as_lines("input/04.txt")
loop1(lines)
loop2(lines)

