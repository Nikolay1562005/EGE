def f(x, a):
    return (x&107 == 0) <= ((x&55 != 0) <= (x&a != 0))

for a in range(1, 3000):
    if all(f(x, a) for x in range(1, 3000)):
        print(a)
        break