with open('27B_2754.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
q = a[:4]
a = a[4:]
mx = 0
k = [[float('inf'), float('inf')] for i in range(137)]
for i in a:
    ost = 0 if i%137 == 0 else i%137
    if k[ost][0] != float('inf'):
        mx = max(mx, abs(i - k[ost][0]))
    if k[ost][1] != float('inf'):
        mx = max(mx, abs(i - k[ost][1]))

    p = q.pop(0)
    k[p % 137][0] = min(p, k[p%137][0])
    k[p % 137][1] = max(p, k[p%137][1])
    q.append(i)
print(mx)