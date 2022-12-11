import re 
import math

class Monkey:
    def __init__(self, input) -> None:
        self.id = int(re.search(r"Monkey (\d+):", input[0])[1])
        self.testDiv = int(re.search(r".+ (\d+)", input[3])[1])
        self.operation = re.search(r"Operation: new = (.+)", input[2])[1]
        self.trueId = int(re.search(r".+ (\d+)", input[4])[1])
        self.falseId = int(re.search(r".+ (\d+)", input[5])[1])
        self.items = [int(item) for item in re.search(r"Starting items: (.+)", input[1])[1].split(', ')]
        self.inspects = 0
        print(' ID', self.id, self.testDiv, self.operation, self.trueId, self.falseId, self.items)

    def __repr__(self) -> str:
        return "{" +'ID '+str(self.id)+', items: '+ ", ".join([str(i) for i in self.items])+" }"

    def worryLevel(self, old):
        return eval(self.operation)
    
    def throwItems(self, monkeys):
        items = self.items
        self.items = []
        for item in items:
            self.inspects +=1
            worryLevel = math.floor(self.worryLevel(item) / 3)
            print(item, worryLevel, worryLevel % self.testDiv)
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
    return monkeys

def loop(monkeys):
    for round in range(0,20):
        for m in monkeys:
            print('\nMONKE', m.id)
            m.throwItems(monkeys)
        print('\nRound',round+1,": ")
        print(monkeys)
            

with open("11.txt") as f:
    input = [x.strip() for x in f]
    monkeys = parse(input)
    loop(monkeys)

    inspects= [m.inspects for m in monkeys]
    inspects.sort(reverse=True)
    print('Part 1:', inspects[0]*inspects[1])

