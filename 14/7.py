b = 4**1014 + 12
for x in range(1, 10000):
    s = b - 2**x
    if bin(s)[2:].count('0') == 2000:
        print(x)
        break