def Del(n,m):
    return n%m == 0
for a in range(1,1000):
    a_true=True
    for x in range(1,1000):
        if not(Del(x, a))<=(not(Del(x, 21) and not(Del(x, 35))))== False:
            a_true=False
            break
    if a_true== True:
        print(a)