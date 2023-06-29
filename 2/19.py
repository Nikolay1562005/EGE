from itertools import *

def f(x,y,z,w):
    return (x and z) or ((w <= x) == (z <= y))

for i in product([0,1], repeat=6):
    table = [
        (i[0], i[1], i[2], 1),
        (i[3], i[4], 1, 1),
        (i[5], 1, 1, 1)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(''.join(list(p)))