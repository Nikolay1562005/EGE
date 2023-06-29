from itertools import *

def f(x,y,z,w):
    return (x==(not(z))) <= ((x or w) == y)

for i in product([0,1], repeat=5):
    table = [
        (0, i[0], 0, i[1]),
        (i[2], i[3], 0, 0),
        (i[4], 0, 0, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,r))) for r in table] == [0, 0, 0]:
                print(''.join(p))