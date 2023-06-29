from itertools import *

with open('27B_2730.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

k = 0
for i in combinations(a, 4):
    if (i[0]*i[1]*i[2]*i[3]) % 12 == 0:
        k = max(k, sum(i))
print(k)
'''
k = []
k_2 = []
k_3 = []
k_4 = []
k_6 = []
k_12 = []

for i in a:
    if i % 12 == 0: k_12.append(i)
    elif i % 6 == 0: k_6.append(i)
    elif i % 4 == 0: k_4.append(i)
    elif i % 3 == 0: k_3.append(i)
    elif i % 2 == 0: k_2.append(i)
    else: k.append(i)

k.sort()
k_2.sort()
k_3.sort()
k_4.sort()
k_6.sort()
k_12.sort()

b = k[-4:] + k_2[-4:] + k_3[-4:] + k_4[-4:] + k_6[-4:] + k_12[-4:]

x = 0
for i in combinations(b, 4):
    if (i[0]*i[1]*i[2]*i[3]) % 12 == 0:
        x = max(x, sum(i))
print(x)'''