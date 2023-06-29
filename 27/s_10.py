with open('27B_2908.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

q = a[:6]
a = a[6:]
mx = float('-inf')
d = [float('inf')]*7
k = len([i for i in q if i > 0 and i % 7 == 0])
s = sum(q)
h = 0
k0 = 0
for i in a:
    s += i
    if i > 0 and i % 7 == 0: k += 1
    if k % 7 == 0: mx = max(s, mx)
    p = s - d[k % 7]
    mx = max(p, mx)

    j = q.pop(0)
    if j > 0 and j % 7 == 0: k0 += 1
    h += j
    d[k0 % 7] = min(d[k0 % 7], h)
    q.append(i)

print(mx)