def f(s, m):
    if s >= 2163: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 1, m -1), f(s * 3, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)

for s in range(1, 2162):
    for m in range(1, 6):
        if f(s, m):
            if m == 4:
                print(s)
            break