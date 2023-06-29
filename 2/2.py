from itertools import *

def f(a, b, c):
    return (a and (not(c))) or ((not(b)) and (not(c)))

t = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
]
for p in permutations('abc'):
    if [f(**dict(zip(p, r))) for r in t] == [1, 0, 0, 0, 1, 0, 1,0]:
        print(''.join(p))