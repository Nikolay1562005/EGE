def f(a, b, m):
    if a + b <= 20: return m % 2 == 0
    if m == 0: return 0
    h = [f(a -1, b, m-1), f(a - int(a/2), b, m-1), f(a, b - 1, m-1), f(a, b - int(b/2), m-1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)

for s in range(11, 100):
    for m in range(1, 6):
        if f(10, s, m):
            if m == 4:
                print(s)
            break