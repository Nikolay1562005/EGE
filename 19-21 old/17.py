#  № 4331 Пробный 06.2022 /dev/inf advanced (Уровень: Сложный)
def f(a, c, m):
    if 124<a<164: return c%2==m%2
    if c==m: return 0
    h = [f(a+2,c+1,m),f(a+4,c+1,m),f(a*2,c+1,m)]
    if c == 2:
        h = [f(a+2,c+1,m),f(a+4,c+1,m)]
    return any(h) if (c+1)%2==m%2 else any(h)

for b in range(1, 124):
    for m in range(1, 8):
        if f(b, 0, m)==1:
            if m == 2:
                print(m, b)
            break
