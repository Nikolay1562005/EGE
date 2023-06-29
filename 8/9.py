from itertools import *

k = 0

for i in product('234', '01234', '01234', '01234', '01234', '012'):
    k += 1
print(k)