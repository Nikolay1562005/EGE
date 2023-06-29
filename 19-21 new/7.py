def f(s, d, e, m):
    if s + d + e >= 73: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 3, d, e, m-1), f(s + 13, d, e, m-1),  f(s + 23, d, e, m-1),
         f(s, d + 3, e, m-1), f(s, d + 13, e, m-1), f(s, d + 23, e, m-1),
         f(s, d, e + 3, m-1), f(s, d, e + 13, m-1), f(s, d, e + 23, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)  # если после неудачного хода то any(h)

for s in range(1, 24):
    for m in range(1, 6):
        if f(2, s, 2*s, m):
            if m == 4:
                print(s)
            break