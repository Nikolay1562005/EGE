from itertools import *

with open('27A_2726.txt') as f:
    n = f.readline()
    a = [int(i) for i in f]

k = max([i for i in a if i%2 == 1]) + max([i for i in a if i%2 == 0])

print(k)