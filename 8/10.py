from itertools import *

k = 0

for i in product('ВИНЯ', 'ВИШНЯ', 'ВИШНЯ', 'ВИШНЯ', 'ВИШНЯ', 'ВШН'):
    i = ''.join(i)
    if i.count('В') <= 1:
        k += 1
print(k)