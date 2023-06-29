with open('27A_2724.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
count = 0
k = [0]*131
for j in a:
    ost = (131 - j % 131) % 131
    count += k[ost]
    k[j % 131] += 1
print(count)