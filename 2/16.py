from itertools import *

def f(x,y,z,w):
    return (not(z and (not(w)))) or ((z <= w) == (x <= y))

for i in product([0, 1], repeat=6):
    t = [
        (1, i[0], i[1], i[2]),
        (1, 1, i[3], 1),
        (1, i[4], i[5], 1)
    ]
    if len(set(t)) == 3:
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(''.join(p))