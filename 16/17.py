def f(n):
    k = 1
    if n >= 1:
        k += 2 + f(n-1) + f(n-3)
    return k
print(f(40))