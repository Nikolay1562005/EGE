from itertools import *

a = "АИОУ"
b = "БКЛН"
k = 0
for i in permutations('АБИКОЛУН', ):
    if i[0] in a and i[2] in a and i[4] in a and i[6] in a:
        if i[1] in b and i[3] in b and i[5] in b and i[7] in b:
            k += 1
for i in permutations('АБИКОЛУН'):
    if i[0] in b and i[2] in b and i[4] in b and i[6] in b:
        if i[1] in a and i[3] in a and i[5] in a and i[7] in a:
            k += 1
print(k)