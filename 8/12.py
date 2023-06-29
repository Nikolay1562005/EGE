from itertools import *

k = 0

for i in product('ГЕПРД', 'ГЕПАРД', 'ГЕПАРД', 'ГЕПАРД', 'ГПАРД'):
    i = ''.join(i)
    if i.count('Г') == 1:
        k += 1
print(k)