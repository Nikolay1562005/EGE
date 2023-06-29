def f(s, d, m):
    if s*d >= 63: return m % 2 == 0
    if m == 0: return 0
    h = [f(s+1, d, m-1), f(s*2, d, m-1), f(s, d+1, m-1), f(s, d*2, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)

for d in range(1, 31):
    for m in range(1, 6):
        if f(2, d, m):
            if m == 4:
                print(d)
            break