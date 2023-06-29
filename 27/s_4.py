with open('27B_2256.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

mx = float('-inf')
d = [float('inf')]*3
k = 0
s = 0
for i in a:
    s += i
    if i % 5 == 0: k += 1
    if k % 3 == 0: mx = max(s, mx)
    if d[k % 3] != float('inf'):
        p = s - d[k % 3]
        mx = max(p, mx)

    d[k % 3] = min(s, d[k % 3])
print(mx)