import aoc
import re

def loop(times, distances):
    res = 1
    for i in range(0,len(times)):
        start = -1
        end = -1
        
        #find start
        for j in range(times[i]):
            x = times[i] - j
            if x*j > distances[i]:
                start = j
                break;
        
        #find end
        for j in range(times[i]-1, 0, -1):
            x = times[i] - j
            if x*j > distances[i]:
                end = j
                break;
        
        res *= (end - start + 1)
    print(res)
                
lines = aoc.input_as_lines("input/06.txt")

#part 1
times = list(map(int,re.findall(r'\d+', lines[0])))
distances = list(map(int,re.findall(r'\d+', lines[1])))
print('part 1:')
loop(times, distances)

#part 2
times = list(map(int,re.findall(r'\d+', lines[0].replace(" ", ""))))
distances = list(map(int,re.findall(r'\d+', lines[1].replace(" ", ""))))
print('part 2:')
loop(times, distances)