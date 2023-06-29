b = 4**2015 - 2**2015 + 15
for x in range(1, 100000):
    s = b + 2**x
    if bin(s)[2:].count('1') == 500:
        print(x)
        break