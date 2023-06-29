def f(x, a):
    return (((x&13 != 0) or (x&a != 0)) <= (x&13 != 0)) or ((x&a != 0) and (x&39 == 0))

for a in range(3000, 1, -1):
    if all(f(x, a) for x in range(1, 3000)):
        print(a)
        break