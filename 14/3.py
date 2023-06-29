s = 2*27**7 + 3**10 - 9
a = []
while s > 0:
    a = [s%3] + a
    s //=3
print(a.count(0))