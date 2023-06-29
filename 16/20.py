
def f(n):
    if n < 3: return n + 1
    elif n >= 3:
        if n%2 == 0: return f(n-2) + n - 2
        else: return f(n+2) + n + 2

k = 0
for i in range(3, 1000):
    try:
        if 10_000 <= f(i) <= 99_999:
            k += 1
    except:
        pass
print(k)