s = 64**30 + 2**300 -4
a = []
while s > 0:
    a = [s%8] + a
    s = s//8
print(a.count(7))