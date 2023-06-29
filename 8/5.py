from itertools import *

k = 0
for i in product('САЛО', repeat=6):
    if 1 <= i.count('О') <= 3:
        k += 1
print(k)