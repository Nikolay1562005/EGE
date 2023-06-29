#5154 - kompege.ru
from sys import *
from functools import *
from threading import *

setrecursionlimit(100_000)
stack_size(200_000_000)


@lru_cache(None)
def f(n):
    if n <= 100_000: return f(n + 1) + 5*n + 2
    elif n > 100_000: return n


for i in range(110_000, 3, -1):
    f(i)
print(f(3) - f(7))
'''
f(3) = f(4) + 15 + 2 = f(5) + 20 + 2 + 17 = f(6) + 25 + 2 + 39 = f(7) + 30 + 2 + 66
f(3) = f(7) + 98
Ответ: 98
'''