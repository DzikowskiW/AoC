import aoc
import re
from collections import defaultdict

cards = '23456789TJQKA'
cardsV= '23456789abcdefghijk'

cardCache = dict()
def cardValue(card, cardsN=cards, cardsV=cardsV):
    
    print('----')
    print(card)
    res = ''
    cards = defaultdict(int)
    for c in card:
        cards[c] += 1
    
    cardvals = list(cards.values())
    if 5 in cards.values():
        res = '7|'
    elif 4 in cards.values():
        res = '6|'
    elif 3 in cards.values() and 2 in cards.values():
        res = '5|'
    elif 3 in cards.values():
        res = '4|'
    elif cardvals.count(2) == 2:
        res = '3|'
    elif 2 in cardvals:
        res = '2|'
    elif 1 in cardvals:
        res = '1|'
    res +=  ''.join(cardsV[cardsN.rfind(c[0])] for c in card)
    print(cardvals)
    print(res)
    return res
    
        

def compareCards(card1, card2):
   return cardValue(card1[0]) - cardValue(card2[0])

def loop(lines):
    lines = list(map(lambda l: l.split(" "), lines))
    lines = list(map(lambda l: (l[0], int(l[1])), lines))
    for i, l in enumerate(lines):
        lines[i] = (cardValue(l[0]), l[0], l[1])
    hand = sorted(lines)
    res = 0
    for i, h in enumerate(hand, start=1):
        print(h)
        res += i*h[2]
    print(res)
lines = aoc.input_as_lines("input/07.txt")

print('part 1:')
loop(lines)

# 250754618 too low
# 250951660