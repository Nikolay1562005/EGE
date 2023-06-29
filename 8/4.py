from itertools import *

k = 0
for i in product('ЛОДКА', repeat=4):
    if i.count('О') >= 2:
        k += 1
print(k)