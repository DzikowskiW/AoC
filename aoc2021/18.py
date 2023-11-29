import ast
import math
import re

def split(num):
    return [math.floor(num/2.0), math.ceil(num/2.0)]

# def analyze(num, depth):
#     if (isinstance(num, int)): return num
#     if (depth < 4):
#         return [analyze(num[0], depth + 1), analyze(num[1], depth +1)]

#     #depth to normalize
#     left = num[0]
#     right = num[1]
#     stable = False
#     while not stable:
#         stable = True
#         if isinstance(left, int) and left >= 10:
#             # left split
#             stable = False
#             left = split(left)
#             continue

#         if isinstance(left, list):
#             #left explode
#             left = [analyze(left[0], depth + 1), analyze(left[1], depth + 1)]
#             if (isinstance(right, int)):
#                 right += left[1]
#             left = 0
#             stable = False

#         if isinstance(right, int) and right >= 10:
#             # right split
#             stable = False
#             right = split(right)
#             continue

#         if isinstance(right, list):
#             # right explode
#             right = [analyze(right[0], depth + 1), analyze(right[1], depth + 1)]
#             if isinstance(left, int):
#                 left += right[0]
#             right = 0
#             stable = False

#     return [left, right]

# def p1(nums):
#     sum = nums[0]
#     for i in range(1, len(nums)):
#         sum =  analyze([sum, nums[i]], 1)
#     print('sum', sum)
#     return 0

def explodeStr(s, i):
    right = i
    left = i
    while (i > 0):
        i -= 1
        c = s[i]
        if c == '[':
            left = i
            break

    [l,r] = s[left+1:right].split(',')
    l = int(l)
    r = int(r)
    
    #find left pos to add num
    leftStr = s[:left]
    if s[:left+1] == ',': leftStr += ','
    matchedLeft = re.match(r'(^.*)(\d+)([\]\[\,]+$)', leftStr)
    if matchedLeft is not None:
        leftStr = matchedLeft.group(1) + str(l + int(matchedLeft.group(2))) + matchedLeft.group(3)

    
    #find right pos to add num
    rightStr = ''
    if s[right:] == ',': rightStr += ','
    rightStr += s[right+1:]
    matchedRight = re.match(r'(^[\]\[\,]+)(\d+)(.*$)', rightStr)
    if matchedRight is not None:
        rightStr = matchedRight.group(1) + str(r + int(matchedRight.group(2))) + matchedRight.group(3)

    newStr = leftStr + '0' + rightStr
    
    # print('str to explode',s[left:right+1])
    # print('new str', newStr)

    return newStr

def splitStr(s, i):
    print('SPLIT', s[:i], s[i], s[i+1], s[i+2:])
    val = int(s[i]+s[i+1])
    return s[:i] + '[' + str(math.floor(val/2.0)) + ',' + str(math.ceil(val/2.0)) + ']' + s[i+2:]

def analyzeStr(numStr):
    nestedCount = 0
    i =0
    while i < len(numStr)-1:
        c = numStr[i]
        if c == '[': 
            nestedCount += 1
        if c == ']': 
            if nestedCount > 4:
                numStr = explodeStr(numStr, i)
                i = 0
                nestedCount = 0
                continue
            nestedCount -= 1
        if (c + numStr[i+1]).isnumeric():
            numStr = splitStr(numStr, i)
            i = 0
            nestedCount = 0
            continue
        i += 1
    return numStr

def p1Str(numLines):
    sum = numLines[0]
    for i in range(1, len(numLines)):
        print(sum, '+', numLines[i])
        sum = analyzeStr('[' + sum + ',' + numLines[i] + ']')
    return sum
    



with open("18.txt") as f:
    lines = [x.strip() for x in f]
    nums = []

    # for line in lines:
    #     nums.append(ast.literal_eval(line))
    
    print('P1', p1Str(lines))

    #print('P1', p1({ 'x': startX, 'y': startY }, { 'x': endX, 'y': endY}))