with open('27B_2907.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

mx = float('-inf')
d = [float('inf')]*30
k = 0
s = 0
for i in a:
    s += i
    if i > 0 and i%2 == 0: k += 1
    ost = k % 30
    if ost == 0:
        mx = max(mx, s)
    p = s - d[ost]
    mx = max(mx, p)

    d[ost] = min(d[ost], s)
print(mx)