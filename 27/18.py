from itertools import *

with open('27B_2736.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

b = [0]*10

for i in a:
    i = list(map(int, str(i)))
    for j in i:
        b[j] += 1
print(min(b))