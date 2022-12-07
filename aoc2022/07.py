import re

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)
    
    def totalSize(self):
        return self.size

    def __str__(self):
        return self.name

class Dir: 
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

    
    def addDir(self, d):
        self.dirs.append(d)

    def addFile(self, f):
        self.files.append(f)

    def totalSize(self):
        sum = 0
        for f in self.files:
            sum += f.totalSize()
        for d in self.dirs:
            sum += d.totalSize()
        return sum
    
    def __repr__(self):
        return self.name

    def __str__(self):
        s = 'D'+self.name + ' ('
        for d in self.dirs:
            s+= str(d)
        for f in self.files:
            s+= str(f) +', '
        s+= ') '
        return s

    def allDirs(self):
        l = [self]
        for d in self.dirs:
            l += d.allDirs()
        return l

def loop(lines):
    isLs = False;
    currentDir = None;
    root = None;
    for line in lines:
        if line[0] == '$' and isLs:
            isLs = False
        if line[:5] == '$ cd ':
            nextPath = line[5:]
            if (nextPath == '/'):
                root = Dir(nextPath, False)
                currentDir = root
            elif (nextPath == '..'):
                currentDir = currentDir.parent
            else:
                d = Dir(nextPath, currentDir)
                currentDir.addDir(d)
                currentDir = d
        if line == '$ ls':
            isLs = True
            continue
        if isLs:
            if line[:3] == 'dir':
                continue
            l = line.split(' ')
            f = File(l[1], l[0])
            currentDir.addFile(f) 

    #part 1
    s = 0
    cap = 100000
    for d in root.allDirs():
        ds = d.totalSize()
        if (ds <= cap):
            s +=ds
    print('Part1:', s)

    #part 2
    maxUsed = 40000000
    toFree = root.totalSize() - maxUsed
    sizes = []
    for d in root.allDirs():
        ds = d.totalSize()
        if (ds >= toFree ):
            sizes.append(ds)
    print('Part 2:', min(sizes))

with open("07.txt") as f:
    lines = [x.strip() for x in f]        
    loop(lines)


