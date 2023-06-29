from itertools import *

k = 0

for i in product("ABCD", repeat=4):
    if i[0] <= i[1] and  i[1] <= i[2] and i[2] <= i[3]:
        k += 1
print(k)