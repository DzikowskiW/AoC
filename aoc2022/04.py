import re

def loop(regExGroups):
    p1 = 0
    p2 = 0
    for g in regExGroups:
        s1 = set(range(g[0], g[1] + 1))
        s2 = set(range(g[2], g[3] + 1))
        if s1.issubset(s2) or s2.issubset(s1):
            p1 += 1
        p2 += int(bool(s1 & s2))
    print('Part 1:', p1)
    print('Part 2:', p2)

with open("04.txt") as f:
    lines = [x.strip() for x in f]
    ob = []
    for line in lines:
        reg = re.search(r"(\d+)\-(\d+)\,(\d+)\-(\d+)", line)
        ob.append(list(map(lambda g: int(g), reg.groups())))

    loop(ob)



