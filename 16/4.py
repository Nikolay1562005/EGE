#5154 - kompege.ru
from functools import *

@lru_cache(None)
def f(n):
    if n <= 3: return n
    elif n > 3:
        if n % 2 == 0: return n**2 + f(n-1)
        else: return 2*n + f(n-2)

for i in range(1, 10_000):
    f(i)
print(f(10_000) - f(9995))