# № 6361 (Уровень: Средний)
def f(a, b, c, m):
    if a+b>39: return c%2==m%2
    if c==m: return 0
    h = []
    if a<b:
        for i in range(1, a):
            h +=[f(a+int(i),b,c+1,m)]
    if b<a:
        for i in range(1, b+1):
            h +=[f(a,b+int(i),c+1,m)]
    if a==b:
        for i in range(1, a+1):
            h +=[f(a+int(i),b,c+1,m)]
            h +=[f(a,b+int(i),c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
s =[]
for b in range(1, 36):
    for m in range(1, 6):
        if f(4, b, 0, m)==1:
            if m == 3:
                s.append(b)
                print(m, b)
            break
print(min(s))
print(max(s))
