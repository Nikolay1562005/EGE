# № 5924 (Уровень: Средний)
def f(a, c, m):
    if a>55 or b>55: return c%2==m%2
    if c==m: return 0
    h = [f(a+1,c+1,m),f(a+2,c+1,m)]
    if a%3==0:
        h +=[f(a*3,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for b in range(1, 55):
    for m in range(1, 8):
        if f(b, 0, m)==1:
            if m == 6:
                print(m, b)
            break
