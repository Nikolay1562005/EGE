with open('27B_1877.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

d = [[float('inf'), 0] for i in range(69)]
mx = [float('-inf'), float('inf')]
s = 0
for i, b in enumerate(a):
    s += b
    ost = s % 69
    if ost == 0:
        mx[0] = s
        mx[1] = i + 1
    if d[ost][0] != float('inf'):
        p = s - d[ost][0]
        j = i + 1 - d[ost][1]
        if p > mx[0] or (p == mx[0] and j < mx[1]):
            mx[0] = p
            mx[1] = j

    if s < d[ost][0]:
        d[ost][0] = s
        d[ost][1] = i + 1

print(mx[1])