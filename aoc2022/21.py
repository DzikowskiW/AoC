import re

OPS = {
    '+': lambda a,b: a + b,
    '-': lambda a,b: a - b,
    '/': lambda a,b: a // b,
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
    
    def calc(self, monkes) -> int:
        if self.val:
            return self.val
        if type(self.left) is not int:
            self.left = monkes[self.left].calc(monkes)
        if type(self.right) is not int:
            self.right = monkes[self.right].calc(monkes)
        return OPS[self.op](self.left, self.right)
        
    
    
with open("aoc2022/21.txt") as f:
    lines = [x.strip() for x in f]
    monkes = {}
    deps = {}

    for l in lines:
        name, rest = l.split(': ')
        monkes[name] = Node(name, rest)
        
    print(monkes['root'].calc(monkes))    
    
