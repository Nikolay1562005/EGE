from itertools import *

k = 0
for i in product('ПУЛЯ', repeat=6):
    if i.count('У') == 2:
        k += 1
print(k)