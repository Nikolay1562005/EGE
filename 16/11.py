cache = {}
def f(n):
    if n == 1: return 1
    if n > 1: return f(n-1) -2*g(n-1)


def g(n):
    if n not in cache:
        if n == 1: cache[i] = 1
        if n > 1: cache[n] = f(n-1) + g(n-1) + n
    return cache[n]

for i in range(1, 36):
    g(i)
print(sum(map(int, str(g(36)))))