for x in range(21, 30):
    s = x
    a = []
    while s > 0:
        a = [s%3] + a
        s //= 3
    if a[-2:] == [1, 1]:
        print(x)