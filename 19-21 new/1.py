def f(s, m):
    if s > 33: return m % 2 == 0
    if m == 0: return 0
    h = [f(s+1, m-1), f(s+5, m-1), f(s*4, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)

for s in range(1,472 + 1):
    for m in range(1, 6):
        if f(s, m) == 1:
            if m == 3:
                print(s)
            break
