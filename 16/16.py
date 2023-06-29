def f(n):
    if n == 1: return 1
    elif n >= 2:
        if n%2 == 0: return f(n//2) + 1
        else: return f(n-1) + n

for i in range(1, 1000):
    if f(i) == 19:
        print(i)
        break