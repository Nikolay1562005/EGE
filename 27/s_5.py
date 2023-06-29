with open('27B_2903.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

mn = float('inf')
d = [float('-inf')]*n
k = 0
s = 0
for i in a:
    s += i
    if i % 3 == 0: k += 1
    if k == 10:
        mn = min(mn, s)
    if k > 10:
        p = s - d[k - 10]
        mn = min(p, mn)

    d[k] = max(d[k], s)
print(mn)