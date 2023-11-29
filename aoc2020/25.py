import collections
import math
import re
import sys

a, b = [9232416, 14144084]

def root(a):
    for i in range(100000000):
        if pow(7, i, 20201227) == a:
            return i
print(root(a))
print(pow(a, root(b), 20201227))
print(pow(b, root(a), 20201227))