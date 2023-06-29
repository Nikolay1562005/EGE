def f(x, y, a):
    return (2*x + y != 70) or (x < y) or (a < x)


for a in range(3000, 1, -1):
    if all(f(x, y, a) for x in range(1, 300) for y in range(1, 300)):
        print(a)
        break