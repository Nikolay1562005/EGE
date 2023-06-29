from itertools import *

k = 0
for i in permutations('ИГРОК'):
    print(i)
    i = ''.join(i)
    if i.count('РОК') == 0 and i[0] != 'К':
       k += 1
print(k)