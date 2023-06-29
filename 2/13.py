from itertools import *

def f(x,y,z,w):
    return ((w <= y) or (not(y <= z))) and (not(x)) and (not(x == z))

for i in product([0, 1], repeat=5):
    t = [
        (0, i[0], 1, i[1]),
        (1, i[2], i[3], 1),
        (0, i[4], 1, 1)
    ]
    if len(set(t)) == 3:
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(''.join(p))