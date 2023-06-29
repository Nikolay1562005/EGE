with open('27B_2363.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

count = 0
q = a[:4]
a = a[4:]
d = [0]*117
s = sum(q)
h = 0
for b in a:
    s += b
    ost = s % 117
    if ost == 0: count += 1
    count += d[ost]

    h += q.pop(0)
    d[h%117] += 1
    q.append(b)
print(count)