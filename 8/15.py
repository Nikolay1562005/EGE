from itertools import *

k = 0

for i in permutations("ВАЙФУ", r=4):
    i = ''.join(i)
    if "ВФ" not in i and "ФВ" not in i and i[0] != 'Й':
        k += 1

print(k)