s = 3*16**8 - 4**5 + 3
a = []
while s != 0:
    a = [s%4] + a
    s = s//4
print(a.count(3))