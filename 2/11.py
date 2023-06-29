from itertools import *

def f(x,y,z,w):
    return (y <= x) or (not((x <= z) and (z <= x))) and (not(w))

for i in product([0, 1], repeat=6):
    t = [
        (0, 0, 0, i[0]),
        (i[1], 0, 0, i[2]),
        (i[3], i[4], 0, i[5])
    ]
    if len(set(t)) == 3:
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(''.join(p))