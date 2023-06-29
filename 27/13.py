from itertools import *

with open('27B_2729.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
'''
k = 10**10
for i in combinations(a, 3):
    if sum(i) % 11 == 0:
        k = min(k, sum(i))
print(k)
''' 

k = [[] for i in range(11)]
for i in a:
    k[i%11].append(i)

b = []

for i in k:
    i.sort()
    b += i[:3]

k = 10**10
for i in combinations(b, 3):
    if sum(i) % 11 == 0:
        k = min(k, sum(i))
print(k)