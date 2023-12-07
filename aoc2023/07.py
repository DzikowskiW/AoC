import aoc
from collections import defaultdict

CARDS = '23456789TJQKA'
CARD_VALS= '23456789abcdefghijk'
CARD_VALS_W_JOKER= '23456789a1cdefghijk'

def card_score(card, is_joker = False, cards=CARDS, card_vals=CARD_VALS):
    score = ''
    
    #count card occurences
    card_counter = defaultdict(int)
    num_of_jokers = 0
    for c in card:
            if c != 'J' or not is_joker:
                card_counter[c] += 1
            else:
                num_of_jokers += 1;
    card_counts = sorted(list(card_counter.values()), reverse=True)
    
    #score card
    if (len(card_counts) == 0):
        return '7' + ''.join(card_vals[cards.rfind(c[0])] for c in card)
    card_counts[0] += num_of_jokers
    if 5 in card_counts:
        score = '7'
    elif 4 in card_counts:
        score = '6'
    elif 3 in card_counts and 2 in card_counts:
        score = '5'
    elif 3 in card_counts:
        score = '4'
    elif card_counts.count(2) == 2:
        score = '3'
    elif 2 in card_counts:
        score = '2'
    elif 1 in card_counts:
        score = '1'
    score +=  ''.join(card_vals[cards.rfind(c[0])] for c in card)
    return score
    
def compareCards(card1, card2):
   return card_score(card1[0]) - card_score(card2[0])

def loop(lines, jokers = False):
    #parse line as tuple (hand, bid)
    lines = list(map(lambda l: l.split(" "), lines))
    lines = list(map(lambda l: (l[0], int(l[1])), lines))

    #score and sort cards
    card_vals= CARD_VALS_W_JOKER if jokers else CARD_VALS
    for i, l in enumerate(lines):
        lines[i] = (card_score(l[0], is_joker=jokers, card_vals=card_vals), l[0], l[1])
    hand = sorted(lines)
    
    res = sum([i*h[2] for i, h in enumerate(hand, start=1)])
    print(res)

lines = aoc.input_as_lines("input/07.txt")
print('part 1:')
loop(lines, jokers = False)
print('part 2:')
loop(lines, jokers = True)
