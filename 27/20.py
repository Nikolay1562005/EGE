from itertools import *

with open('27B_2735.txt') as f:
    n = int(f.readline())
    a = [list(map(int, i.split(' '))) for i in f]

ox = 0
oy = 0
xy = 0

for i in a:
    if i[0] == 0: oy += 1
    elif i[1] == 0: ox += 1
    else: xy += 1

print(xy*ox*oy)