from collections import defaultdict


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
    

def loop(workflow, inputs):
    res = 0
    for input in inputs:
        res += proccess(workflow, input)
    print('Part 1', res)

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
    
    loop(workflow, inputs)
   