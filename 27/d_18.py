with open('27B_2759.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            if a[i] + a[j] <= 134:
                count += 1

print(count)