import re

OPS = {
    '+': lambda a,b: a + b,
    '-': lambda a,b: a - b,
    '/': lambda a,b: a / b,
    '*': lambda a,b: a * b,
}

class Node:
    def __init__(self, name, rest):
        self.name = name
        self.val = None
        self.left = None,
        self.right = None
        self.op = None
        num = re.match(r'(\d+)', rest)
        if num:
            self.val = int(num.group(0))
        else:
            self.left, self.op, self.right = re.match(r'(\w+) (.) (\w+)', rest).groups()
        
    def __repr__(self) -> str:
        s = self.name + ": "
        if self.val is not None:
            s += str(self.val)
        else: 
            s += self.left + self.op + self.right
        return s
    
    def calc(self, monkes, vals) -> int:
        if type(self.val) is int:
            return self.val
        
        if self.left not in vals:
            vals[self.left] = monkes[self.left].calc(monkes, vals)
        if self.right not in vals:
            vals[self.right] = monkes[self.right].calc(monkes, vals)
        return OPS[self.op](vals[self.left], vals[self.right])
    
    def hasHumn(self, monkes):
        if self.name == 'humn':
            return True
        if self.left is None or self.right is None:
            return False
        return monkes[self.left].hasHumn(monkes) or monkes[self.right].hasHumn(monkes) 
    
        
def part2(monkes):
    root1 = monkes['root'].left
    root2 = monkes['root'].right
    monkes['humn'].val = 1
    if monkes[root1].hasHumn(monkes):
        h = monkes[root1]
        v = monkes[root2]
    else:
        h = monkes[root2]
        v = monkes[root1]

    # monkes['humn'].val = 150
    val = v.calc(monkes, {})
    hum = h.calc(monkes, {})
    print(val)
    print(hum)
    maxH = 10000000000000
    minH = 1
    curH = (maxH-minH) // 2
    while val != hum:
        # if monkes['humn'].val % 100 == 0:
        #     print(monkes['humn'].val, v.calc(monkes, {}), h.calc(monkes, {}))
        monkes['humn'].val += 1
        hum = h.calc(monkes, {})
    return monkes['humn'].val
    
    
    
with open("aoc2022/21a.txt") as f:
    lines = [x.strip() for x in f]
    monkes = {}
    deps = {}

    for l in lines:
        name, rest = l.split(': ')
        monkes[name] = Node(name, rest)
        
    print('part1', int(monkes['root'].calc(monkes, {})))
    print('part2', part2(monkes))
    
      
    
