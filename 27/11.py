with open('27B_2727.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
a.sort()
b_31 = [i for i in a if i % 31 == 0]
b_31.sort()
print(b_31[0]*a[0])