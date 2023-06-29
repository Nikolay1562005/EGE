s = 6*144**26 + 11*12**75 - 48
a = []
while s > 0:
    a = [s%12] + a
    s //= 12
print(a.count(11))