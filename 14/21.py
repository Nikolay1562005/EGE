for x in range(15):
    s = 15**4 + 2*15**3 + 3*15**2 + x*15 + 5 + 15**4 + x*15**3 + 2*15**2 + 3*15 + 3
    if s % 14 == 0:
        print(s//14)
        break