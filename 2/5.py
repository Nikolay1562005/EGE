from itertools import *

def f(x, y, z, w):
    return (x <= (y and (not(z)))) or w

for i in product([0, 1], repeat=6):
    t = [
        (i[0], i[1], 1, 0),
        (0, i[2], i[3], 1),
        (1, i[4], 1, i[5])
    ]
    if len(set(t)) == 3:
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(''.join(p))