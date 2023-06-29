def f(s, d, m):
    if s + d >= 68: return m % 2 == 0
    if m == 0: return 0
    h = [f(s+1, d, m-1), f(s + d, d, m-1), f(s, d+1, m-1), f(s, d + s, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)  # если после неудачного хода то any(h)

for d in range(1,60):
    for m in range(1, 6):
        if f(8, d, m):
            if m == 4:
                print(d)
            break