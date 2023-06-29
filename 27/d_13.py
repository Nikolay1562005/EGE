with open('27B_2761.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

q = a[:5]
a = a[5:]
count = 0
k = [[0]*13, [0]*13]

for i in a:
    ost = i%13
    if i%2 == 0:
        count += k[0][ost] + k[1][ost]
    else:
        count += k[0][ost]

    p = q.pop(0)
    k[p%2][p%13] += 1
    q.append(i)
print(count)