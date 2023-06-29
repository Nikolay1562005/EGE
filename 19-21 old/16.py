#  № 5441 Джобс 21.12.22 (Уровень: Сложный)
def f(a, c, m):
    if a>81: return c%2==m%2
    if c==m: return 0
    h = [f(a+10,c+1,m),f(a*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for b in range(1, 82):
    for m in range(1, 8):
        if f(b, 0, m)==1:
            if m == 2:
                print(m-1, b)
            break
