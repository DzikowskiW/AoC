
class Job:
    def __init__(self, cmd) -> None:
        if cmd == 'noop':
            self.cycles = 1
            self.val = 0
        elif cmd[:4] == 'addx':
            self.cycles = 2
            self.val = int(cmd.split(' ')[1])

    def isDone(self):
        return self.cycles == 0
    
    def valToAdd(self):
        self.cycles -= 1
        if self.cycles == 0:
            return self.val
        return 0

def printPixels(m):
    l=''
    for i in range(0, len(m)):
        if i % 40 ==0 and len(l) > 0:
            print(l)
            l = ''
        l += m[i]
    print(l)


def parse(cmds):
    cycle= 1
    x =1
    loop = True;
    job = Job(cmds.pop(0))

    #part 1
    nextCheck = 20
    strength = 0

    #part 2
    pixels = ['#']

    while loop:
        cycle += 1
        x+= job.valToAdd()
        if job.isDone():
            if len(cmds) == 0: 
                loop = False
            else:
                job = Job(cmds.pop(0))
        
        #part 1
        if cycle == nextCheck:
            nextCheck += 40
            strength += cycle * x
            print('cycle', cycle, 'val', x, 'strength', cycle*x, 'total', strength)
        
        #part 2
        pos = len(pixels) % 40
        sign = '#' if x - 1 <= pos <= x + 1 else '.'
        pixels.append(sign)

    print('\nPart 1:', strength)
    print('-----')
    printPixels(pixels)
        
        

with open("10.txt") as f:
    input = [x.strip() for x in f]
    parse(input)


