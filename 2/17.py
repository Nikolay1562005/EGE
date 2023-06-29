from itertools import *

def f(a,b,c,d):
    return ((not(a)) and (not(b))) or (b == c) or d

for i in product([0,1], repeat=4):
    t = [
        (i[0], i[1], 1, i[2]),
        (1, 0, i[3], 1),
        (0, 0, 1, 1)
    ]
    if len(set(t)) == len(t):
        for p in permutations('abcd'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(''.join(p))