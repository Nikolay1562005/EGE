def f(n):
    if n == 0: return 0
    elif n > 0:
        if n%2 == 0: return f(n//2)
        else: return f(n-1) + 1

k = 0
for i in range(1, 501):
    if f(i) == 8:
        k += 1
print(k)