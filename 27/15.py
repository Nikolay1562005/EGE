from itertools import *

with open('27B_2732.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
a.sort()
'''
k = 0
for i in combinations(a, 2):
    if abs(i[0]-i[1]) % 80 == 0:
        k = max(abs(i[0]-i[1]), k)
print(k)'''

b = [[] for i in range(80)]

for i in a:
    b[i%80].append(i)

c = []
for i in b:
    if i != [] and len(a) > 3:
        i.sort()
        c.append(max(i)-min(i))

print(max(c))