s = 125**200 + 74
for x in range(1, 1000000):
    b = s - 5**x
    a = []
    while b > 0:
        a = [b%5] + a
        b //=5
    if a.count(4) == 100:
        print(x)
        break