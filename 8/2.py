from itertools import *

a = 'WXYZ'
k = 0

for i in product('WXYZ', 'ABC', 'ABC', 'ABC', 'ABC', 'WXYZ'):
        k += 1
print(k)