# № 6051 ФИПИ 04.02.23 (Уровень: Базовый)
def f(a, b, c, m):
    if a+b>51: return c%2==m%2
    if c==m: return 0
    h = [f(a+2,b,c+1,m),f(a*3,b,c+1,m),f(a,b+2,c+1,m),f(a,b*3,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for b in range(1, 47):
    for m in range(1, 8):
        if f(5, b, 0, m)==1:
            if m == 3:
                print(m, b)
            break
