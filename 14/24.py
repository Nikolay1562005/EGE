for x in range(15):
    for y in range(17):
        a = 15**4 + 2*15**3 + 3*15**2 + x*15 + 5 + 6*17**3 + 7*17**2 + y*17 + 9
        if a % 131 == 0:
            print(x, y, a//131)