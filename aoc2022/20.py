# OG val:num -> og_index <----> curr_index <- val:og_index CURR
def calcGrove(og, curr):
    index0 = curr.index(og.index(0))
    v1000= og[curr[(index0 + 1000) % len(curr)]]
    v2000= og[curr[(index0 + 2000) % len(og)]]
    v3000= og[curr[(index0 + 3000) % len(og)]]
    print(v1000, v2000, v3000)
    return v1000 + v2000 + v3000

with open("aoc2022/20.txt") as f:
    lines = [x.strip() for x in f]
    og = []
    
    for l in lines:
        og.append(int(l))
    curr = [i for i in range(0, len(og))]    

    for i,n in enumerate(og):
        curr_i = curr.index(i)
        curr.pop(curr_i)
        index = (curr_i+n) % len(curr)
        if index == 0:
            curr.append(i)
        else:
            curr.insert(index, i)
    
    zero = curr.index(og.index(0))
    
    # print([og[x] for x in curr])
    print(calcGrove(og, curr))
    
    
