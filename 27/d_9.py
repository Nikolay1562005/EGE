with open('27B_2757.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

q = a[:8]
a = a[8:]
count = 0
k = [0]*23
for i in a:
    ost = i % 23
    if ost == 0:
        count += sum(k)
    else:
        for j in range(23):
            if ost*j % 23 == 0:
                count += k[j]

    p = q.pop(0)
    k[p%23] += 1
    q.append(i)
print(count)