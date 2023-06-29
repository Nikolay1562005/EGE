#  №5885 Danov2301 (Уровень: Сложный)
def f(a, c, m):
    if a==42: return c%2==m%2
    if c==m: return 0
    if a<43:
        h = [f(a+1,c+1,m),f(a+3,c+1,m),f(a+7,c+1,m)]
    else:
        h = [f(a-1,c+1,m),f(a-3,c+1,m),f(a-7,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for b in range(1, 55):
    for m in range(1, 8):
        if f(b, 0, m)==1:
            if m == 4:
                print(m, b)
            break
