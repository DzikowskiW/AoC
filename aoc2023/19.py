from collections import defaultdict
from copy import deepcopy

def proccess(workflow, input):
    vals = defaultdict(int)
    for i in input:
        k, v = i.split('=')
        vals[k] = int(v)
    x = vals['x']
    m = vals['m']
    a = vals['a']
    s = vals['s']

    current = 'in'
    while current not in ['A', 'R']:
        for w in workflow[current]:
            if eval(w[0]):
                current = w[1]
                break
    if current == 'A':
        return x + m + a + s
    return 0

def part1(workflow, inputs):
    res = 0
    for input in inputs:
        res += proccess(workflow, input)
    print('Part 1', res)
    
def part2(workflow):
    current = 'in'
    start = {
        'x': (1,4000),
        'm': (1,4000),
        'a': (1,4000),
        's': (1,4000)
    }
    ranges = [('in', start)]
    res = []
    while ranges:
        name, r = ranges.pop(0)
        if name == 'A':
                res.append(deepcopy(r))
                continue
        for w in workflow[name]:
            r = deepcopy(r)
            cond, nxt = w
            if cond == 'True':
                ranges.append((nxt, deepcopy(r)))
                break
            letter = cond[0]
            type = cond[1]
            val = int(cond[2:])
            rltmp = 0
            if type == '<' and r[letter][1] > val and val > r[letter][0]:
                dr = deepcopy(r)
                dr[letter] = (dr[letter][0], val-1)
                ranges.append((nxt, dr))
                r[letter] = (val, r[letter][1])
            elif type == '>' and r[letter][0] < val and val < r[letter][1]:
                dr = deepcopy(r)
                dr[letter] = (val+1, dr[letter][1])
                ranges.append((nxt, dr))
                r[letter] = (r[letter][0], val)

    count = 0
    for r in res:
        sr = 1
        for rr in r.values():
            sr *= rr[1]-rr[0]+1
        count +=sr
    print('part 2:', count)
 

with open("input/19.txt") as f:
    workflowstr, inputs = f.read().rstrip().split('\n\n')
    workflowstr = workflowstr.split('\n')
    workflow = dict()
 
    for w in workflowstr:
        name, rules = w.split('{')
        workflow[name] = rules[:-1].split(',')
        ww = defaultdict(list)
                
    for n in workflow:
        for i,w in enumerate(workflow[n]):
            if ':' in w:
                cond, goto = w.split(':')
                ww[n].append((cond, goto))
            else:
                ww[n].append(('True', w))
    workflow = ww
    inputs = [input[1:-1].split(',') for input in inputs.split('\n')]
    
    part1(workflow, inputs)
    part2(workflow)
   