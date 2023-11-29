import operator
import functools
from collections import defaultdict


def p1(data):
    mapping = {
        2: 1,
        4: 4,
        3: 7,
        7: 8
    }
    d = map(lambda d: d['output'], data) # output only
    d = functools.reduce(lambda flatOut, dataRow: flatOut + dataRow, d, []) # flatten 2d array into 1d
    d = map(lambda val: len(val), d) # replace string with its lengths
    d = filter(lambda val: val in [2, 4, 3, 7], d) # leave only unique numbers
    #d = map(lambda val: mapping[val], d) # map unique numbers to actual numbers
    d = [*d] # do it!
    return len(d)

def p2(data):
    uniqueDigits = {
        2: 1,
        4: 4,
        3: 7,
        7: 8
    }
    sum = 0
    for d in data:
        wires = dict()
        d['input'] = [*map(lambda s: ''.join(sorted(s)), d['input'])] #sort chars
        d['output'] = [*map(lambda s: ''.join(sorted(s)), d['output'])] #sort chars
        input = d['input']
        output = d['output']
        #mark wires
        #select unique digits
        for code in input:
            codeLen = len(code)
            if codeLen in uniqueDigits.keys():
                wires[uniqueDigits[codeLen]] = code
        
        for code in input:
            codeLen = len(code)
            if codeLen == 5 and inStr(code, wires[1]):
                wires[3] = code
            elif codeLen == 6 and inStr(code, wires[4]):
                wires[9] = code
            elif codeLen == 6 and not inStr(code, wires[1]):
                wires[6] = code

        for code in input:
            codeLen = len(code)
            if codeLen == 6 and code != wires[9] and code != wires[6]:
                wires[0] = code
            if codeLen == 5 and code != wires[3] and inStr(wires[9], code):
                wires[5] = code
            if codeLen == 5 and code != wires[3] and not inStr(wires[9], code):
                wires[2] = code
        
        #map output
        mapping = res = dict((v,k) for k,v in wires.items())
        r = 0
        for o in output:
            r = 10* r + mapping[o]
        print('D: ', r)
        sum += r
    return sum

def inStr(s, check):
    for c in check:
        if c not in s: 
            return False
    return True

with open("08.txt") as f:
    lines = [x.strip() for x in f]
    data = []
    for line in lines:
        input, output = line.split(' | ', maxsplit=1)
        data.append({
            'input': input.split(' '),
            'output': output.split(' ')
        })
    
    print(p2(data))