with open('27B_2756.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

mx = float('-inf')
k = [float('-inf')]*100

for i in a:
    ost = i%100
    if ost > 12 and k[112 - ost] > i:
        mx = max(mx, k[112 - ost] + i)
    if ost < 12 and k[12 - ost] > i:
        mx = max(mx, k[12 - ost] + i)

    k[ost] = max(i, k[ost])

print(mx)