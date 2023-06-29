with open('27B_2751.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

q = a[:4]
a = a[4:]
count = 0
k = [[0, 0], [0, 0]]

for i in a:
    if i % 2 == 0:
        if i % 13 == 0:
            count += k[1][0] + k[1][1]
        else:
            count += k[1][1]
    else:
        if i % 13 == 0:
            count += k[0][0] + k[0][1]
        else:
            count += k[0][1]

    p = q.pop(0)
    k[p%2][int(p%13 == 0)] += 1
    q.append(i)
print(count)