from sys import *

setrecursionlimit(3000)


def f(n):
    if n == 1: return 1
    elif n > 1: return n*f(n - 1)


print(f(2023)/f(2020))