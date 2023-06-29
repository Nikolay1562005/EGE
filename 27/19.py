from itertools import *

with open('27A_2731.txt') as f:
    n = int(f.readline())
    s = [list(map(int, i.split(' '))) for i in f]

b_y_0 = []
b = []
for i in s:
    if i[1] == 0: b_y_0.append(i)
    else: b.append(i)
b_y_0 = sorted(b_y_0)
a = abs(b_y_0[0][0]) + abs(b_y_0[-1][0])
h = 0
for i in b:
    h = max(abs(i[1]), h)
print(0.5*a*h)