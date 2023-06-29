with open('27B_2727.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

k = [float('inf')]*31
mn = float('inf')

for i in a:
    ost = 0 if i % 31 == 0 else i % 31
    for j in range(31):
        if ost*j % 31 == 0:
            mn = min(mn, i*k[j])

    k[ost] = min(i, k[ost])
print(mn)