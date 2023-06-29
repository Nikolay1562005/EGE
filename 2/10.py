from itertools import *

def f(x,y,z):
    return (not(x == (y <= z)))


t = [
    (0, 0, 1),
    (0, 1, 1)
]

for p in permutations('xyz'):
    if [f(**dict(zip(p, r))) for r in t] == [1, 0]:
        print(''.join(p))