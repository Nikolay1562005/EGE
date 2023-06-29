from itertools import *

with open('27A_2736.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

b = [0]*10

for i in a:
    i = int(str(i)[0])
    b[i] += 1
print(min(b[1:]))