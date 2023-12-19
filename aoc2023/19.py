from collections import defaultdict



with open("input/19a.txt") as f:
    workflowstr, input = f.read().rstrip().split('\n\n')
    workflowstr = workflowstr.split('\n')
    workflow = dict()
    for w in workflowstr:
        name, rules = w.split('{')
        workflow[name] = rules[:-1].split(',')
        print(workflow[name])
    input = input.split('\n')
    print(workflowstr)
   