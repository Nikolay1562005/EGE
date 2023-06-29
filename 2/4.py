from itertools import *

def f(x, y, z, w):
    return (((not(x)) and y) == z) and w

for i in product([0, 1], repeat=10):
    t = [
        (i[0], 0, i[1], i[2]),
        (i[3], i[4], i[5], 0),
        (0, 0, i[6], i[7]),
        (0, 0, i[8], i[9])
    ]
    if len(set(t)) == 4:
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1, 1]:
                print(''.join(p))