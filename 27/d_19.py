with open('27B_2764.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

q = a[:6]
a = a[6:]
mn = float('inf')
k = [float('inf')]*23

for i in a:
    ost = 0 if i%23 == 0 else 23 - i % 23
    b = i*k[ost]
    if b%6 == 0:
        mn = min(mn, i + k[ost])

    p = q.pop(0)
    k[p%23] = min(p, k[p%23])
    q.append(i)

print(mn)