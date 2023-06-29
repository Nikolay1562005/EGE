from itertools import *

k = []
for i in permutations("МИМИКРИЯ"):
    i = ''.join(i)
    if i not in k:
        k.append(i)
print(len(k))