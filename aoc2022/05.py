import re
import math


with open("05.txt") as f:
    lines = [x for x in f]
    crates = {}

    analyzeCrates = True
    for line in lines:
        if (len(line.strip()) == 0):
            analyzeCrates = False
            print('START: ',crates)
            continue

        if analyzeCrates:
            print(line)
            for i in range(1, len(line), 4):
                if line[i].isupper():
                    print(i, line[i])
                    ci = math.floor((i-1)/4)+1
                    if not ci in crates: 
                        crates[ci] =[]
                    crates[ci].append(line[i])
        else:
            xx, source, dest = re.search(r"move (\d+) from (\d+) to (\d+)", line).groups()
            
            xx= int(xx)
            source= int(source)
            dest = int(dest)

            #part 1
            # for i in range(0, xx):
            #     print('moving ',crates[source][0],'from',source,'to',dest)
            #     val = crates[source].pop(0)
            #     crates[dest].insert(0, val)
            #     print('AFTER: ',crates[4])

            #part 2
            val = crates[source][:xx]
            crates[source] = crates[source][xx:]
            crates[dest] = val + crates[dest]
            print('AFTER: ',crates)


            print('-------')

    i = 1 
    result = ''
    while (i in crates):
        result += crates[i][0]
        i+=1
    print(result)
