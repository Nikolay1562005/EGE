with open('27B_2721.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]


a_5 = [i for i in a if i % 5 == 0 and i % 65 != 0]
a_13 = [i for i in a if i % 13 == 0 and i % 65 != 0]
a_65 = [i for i in a if i % 65 == 0]
k5 = len(a_5)
k13 = len(a_13)
k65 = len(a_65)
knot65 = n - k65
print(k65*(k65-1)//2 + k5*k13 + k65*knot65)