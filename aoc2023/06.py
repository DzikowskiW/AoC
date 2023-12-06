import aoc
import functools
import re
import math
from collections import defaultdict

def loop1(times, distances):
    print(times, distances)
    res = 1
    for i in range(0,len(times)):
        ways = 0
        for j in range(times[i]):
            for x in range (1, times[i] - j+1):
               if x*j > distances[i]:
                   print(j, x, x*j)
                   ways += 1 
                   break
        # print(times[i], distances[i], ways)
        res *= ways
    print(res)
                
                
    
lines = aoc.input_as_lines("input/06.txt")
times = list(map(int,re.findall(r'\d+', lines[0])))
distances = list(map(int,re.findall(r'\d+', lines[1])))
loop1(times, distances)