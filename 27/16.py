from itertools import *

with open('27B_2734.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

b = [0]*50
for i in a:
    i = sum(map(int, str(i)))
    #i = sum([int(x) for x in list(str(i))])
    b[i] += 1
print(max(b))