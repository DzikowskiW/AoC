import re 
import math


class Monkey:
    maxVal = 1

    def __init__(self, input) -> None:
        self.id = int(re.search(r"Monkey (\d+):", input[0])[1])
        self.testDiv = int(re.search(r".+ (\d+)", input[3])[1])
        self.operation = re.search(r"Operation: new = (.+)", input[2])[1]
        self.trueId = int(re.search(r".+ (\d+)", input[4])[1])
        self.falseId = int(re.search(r".+ (\d+)", input[5])[1])
        self.items = [int(item) for item in re.search(r"Starting items: (.+)", input[1])[1].split(', ')]
        self.inspects = 0

    def __repr__(self) -> str:
        return "{" +'ID '+str(self.id)+', items: '+ ", ".join([str(i) for i in self.items])+" }"

    def worryLevel(self, old):
        return eval(self.operation) % Monkey.maxVal
    
    def throwItems(self, monkeys, divideByThree):
        items = self.items
        self.items = []
        for item in items:
            self.inspects +=1
            worryLevel = self.worryLevel(item) 
            if divideByThree: worryLevel = worryLevel // 3
            if worryLevel % self.testDiv == 0:
                monkeys[self.trueId].items.append(worryLevel)
            else:
                monkeys[self.falseId].items.append(worryLevel)


def parseMonkey(monkeys, m):
    monke = Monkey(m)
    monkeys.append(monke)

def parse(input):
    m =[]
    monkeys = []
    for l in input:
        if len(l) ==0:
            parseMonkey(monkeys, m)
            m = []
        else:
            m.append(l)
    if len(m) > 0:
        parseMonkey(monkeys, m)
    for m in monkeys: 
        Monkey.maxVal *= m.testDiv
    return monkeys

def loop(monkeys, rounds, divideByThree):
    for round in range(0,rounds):
        for m in monkeys:
            m.throwItems(monkeys, divideByThree)      

with open("11.txt") as f:
    input = [x.strip() for x in f]
    monkeys = parse(input)
    
    # Part 1
    #loop(monkeys, 20, True)
    
    # Part 2
    loop(monkeys, 10000, False)

    inspects= [m.inspects for m in monkeys]
    inspects.sort(reverse=True)
    print('Result:', inspects[0]*inspects[1])

