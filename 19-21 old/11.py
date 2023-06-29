# № 6091 /dev/inf 02.2023 (Уровень: Базовый)
def f(a, b, c, m):
    if a>478 or b >478: return c%2==m%2
    if c==m: return 0
    h = [f(a+1,b,c+1,m),f(a+3,b,c+1,m),f(a*2,b,c+1,m),f(a,b+1,c+1,m),f(a,b+3,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for b in range(1, 479):
    for m in range(1, 6):
        if f(239, b, 0, m)==1:
            if m == 2:
                print(m, b)
            if m == 4:
                print(m, b)
            break
