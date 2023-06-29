from itertools import *

k = 0

for i in product("AB123", repeat=8):
    i = ''.join(i)
    if i.count("A") + i.count("B") == 2:
        k += 1
print(k)