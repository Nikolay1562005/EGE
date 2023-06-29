with open('27B_2752.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

count = 0
q = a[:5]
a = a[5:]
k = [0]*10
for i in a:
    ost = i % 10
    for j in range(10):
        if ost*j % 10 == 3:
            count += k[j]
    p = q.pop(0)
    k[p%10] += 1
    q.append(i)
print(count)