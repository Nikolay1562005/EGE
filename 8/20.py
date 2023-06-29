from itertools import *

k = 0
s = sorted('АЛГОРИТМ')

for i in product(s, repeat=4):
    k += 1
    if i[-2] + i[-1] == 'ИМ':
        print(k, i)