b = 36**17 + 71
for x in range(1, 100000):
    s = b - 6**x
    a = []
    while s > 0:
        a = [s%6] + a
        s //= 6
    if sum(a) == 61:
        print(x)
        break