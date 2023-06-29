def f(i, m):
    if i > 20: return m%2 == 0
    if m == 0: return 0
    h = [f(i + 1, m - 1), f(i + 2, m - 1), f(i + 3, m - 1)]
    return any(h) if (m-1)%2 == 0 else all(h)

k = 0
for s in range(1, 20 + 1):
    for m in range(1, 100):
        if f(s, m) == 1:
            if m%2 == 0:
                k += 1
            break
print(k)