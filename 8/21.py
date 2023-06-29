from itertools import *

k = 0
for i in product('KOT', repeat=4):
    k += 1
    i = ''.join(i)
    if i == 'KOOOOOT':
        print(i, k)

a = 'KOTKOTKOTKOTKOT'

for i, a in enumerate(a):
    print(i, a)