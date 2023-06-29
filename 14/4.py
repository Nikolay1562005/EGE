s = 51*7**12 - 7**3 - 22
a = []
while s > 0:
    a = [s%7] + a
    s //= 7
print(sum(a))