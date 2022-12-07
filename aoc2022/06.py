import re

def calculateSeq(line, seqLen):
    seq = []
    for i in range(len(line)):
        c = line[i]
        seq.append(c)
        if len(seq) > seqLen:
            seq.pop(0)
        if len(set(seq)) == seqLen:
            return i+1

with open("06.txt") as f:
    lines = [x.strip() for x in f]

    print(calculateSeq(lines[0],4))
    print(calculateSeq(lines[0],14))




