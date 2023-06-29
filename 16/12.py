from functools import *

@lru_cache(None)
def f(n):
    if n == 0: return 1
    if n == 1: return 3
    if n > 1: return f(n-1) - f(n-2) + 3*n

for i in range(0, 40):
    f(i)
print(f(40))