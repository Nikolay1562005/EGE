with open('27B_2755.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

mn = float('inf')
k = [float('inf')] * 144

for i in a:
    ost = i % 144
    if k[(144-ost)%144] < i:
        mn = min(mn, i + k[(144-ost)%144])

    k[ost] = min(i, k[ost])
print(mn)