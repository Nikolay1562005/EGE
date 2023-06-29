def f(x, a):
    return ((x % 4 != 3) or (x % 6 != 1)) <= (x % 36 != a)

for a in range(1, 3000):
    if all(f(x, a) for x in range(1, 3000)):
        print(a)
        break