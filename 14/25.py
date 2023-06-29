def f(x, y):
    return 21**4 + 2*21**3 + y*21**2 + x*21 + 9 + 3*21**4 + 6*21**3 + y*21**2 + 9*21 + 9
for x in range(21):
    for y in range(21):
        if f(x, y) % 18 != 0:
            break
    else:
        print(f(x, 5)//18)
        break