from itertools import *

k = 0

for i in permutations("ДЕЙКСТРА", r=6):
    i = ''.join(i)
    if "ЙД" in i or "ЙК" in i or "ЙС" in i or "ЙТ" in i or "ЙР" in i:
        k += 1
print(k)