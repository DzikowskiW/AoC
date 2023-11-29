import math
import itertools

def mapBeacons(scanner):
    m = []
    for beacon in scanner:
        x, y, z = beacon
        distance = math.sqrt(x*x + y*y + z*z)
        m.append(distance)
    return m

def compare(s1, s2):
    set2 = set(s2)
    matched = []
    for b in s1:
        if b in set2:
            matched.push(b)
    
    print('matched', len(matched))
    return len(matched) >= 12


def p1(scanners):
    beacons = []
    for scanner in scanners:
        beacons.append(mapBeacons(scanner))
    
    for i in range(len(scanners)):
        for j in range(len(scanners)):
            if i != j and compare(beacons[i], beacons[j]):
                print('COMPARED', i, j)
    return 0


with open("19a.txt") as f:
    lines = [x.strip() for x in f]
    scanners = [[]]
    scannerId = 0
    scanners[0]
    for line in lines:
        if len(line) == 0:
            scannerId += 1
            scanners.append([])
            continue
        if line[0] == '-':
            continue
        scanners[scannerId].append([*map(lambda val: int(val),line.split(','))])
    
    print(p1(scanners))