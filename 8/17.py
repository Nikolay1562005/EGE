from itertools import *

k = 0
for i in product(sorted('ЛЕМУР'), repeat=4):
    k += 1
    if i[0] == 'Л':
        print(k)
        break