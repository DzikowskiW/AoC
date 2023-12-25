def process(lines):
    size = 0
    for ll in lines:
        l,w,h = ll
        s1, s2, s3 = 2*l*w, 2*h*w, 2*l*h 
        size += s1 + s2 + s3 + min(s1, s2, s3)//2
    print('part 1:', size)

lines = open("input/02.txt").read().rstrip().split('\n')
lines = [tuple(map(int, dim)) for dim in (ll.split('x') for ll in lines)]    
process(lines)