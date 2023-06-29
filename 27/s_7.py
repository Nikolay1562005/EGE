with open('27B_2904.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

mn = [float('inf'), 0]
d = [[float('-inf'), 0] for i in range(2077)]
s = 0
for i, b in enumerate(a):
    s += b
    ost = s % 2077
    if ost == 0:
        if s < mn[0] or s == mn[0] and (i+1) > mn[1]:
            mn[0], mn[1] = s, i + 1
    if d[ost][0] != float('-inf'):
        p = s - d[ost][0]
        j = i + 1 - d[ost][1]
        if p < mn[0] or p == mn[0] and j > mn[1]:
            mn[0], mn[1] = p, j

    if s > d[ost][0]:
        d[ost][0], d[ost][1] = s, i + 1
print(mn[1])