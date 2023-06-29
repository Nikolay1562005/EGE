#5157 - kompege.ru
from functools import *
from sys import *

setrecursionlimit(3000)

@lru_cache(None)
def f(n):
    if n >= 10_000: return n
    else:
        if n % 3 == 0: return n + f(n//3)
        else: return 2*n + f(n+3)

for i in range(10_000, 1, -3):
    f(i)
print(f(999) - f(46))