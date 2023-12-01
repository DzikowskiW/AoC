import aoc
import re

matches = [
    ('on1e', 'one'),
    ('tw2o', 'two'),
    ('thr3ee', 'three'),
    ('fo4ur', 'four'),
    ('fi5ve', 'five'),
    ('s6ix', 'six'),
    ('sev7en', 'seven'),
    ('eigh8t', 'eight'),
    ('ni9ne', 'nine')
]

#first part
def loop(lines):
    summ = 0
    for l in lines:
        digits = re.findall(r'\d', l)
        digits1 = int('' + digits[0] + digits[-1])
        summ += digits1 
    print(summ)

# second part
def loop2(lines):
    summ = 0
    for l in lines:
        ll = l
        while True:
            d = re.search(r'(one|two|three|four|five|six|seven|eight|nine)', l)
            if d is None:
                break
            for digit in matches:
                if (digit[1] == d[1]):
                    l = re.sub(digit[1],str(digit[0]),l,count=1)
        digits = re.findall(r'\d', l)
        digits1 = int('' + digits[0] + digits[-1])
        summ += digits1
    print(summ)
    
lines = aoc.input_as_lines("01.txt")
loop(lines)
loop2(lines)