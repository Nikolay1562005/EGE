s = 5*216**1156 - 4*36**1147 + 6**1153 - 875
a = []
while s > 0:
    a = [s%6] + a
    s //= 6
print(a.count(5) - a.count(0))