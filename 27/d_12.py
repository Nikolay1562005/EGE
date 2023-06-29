with open('27B_2753.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

count = 0

for i in range(n):
    for j in range(i+1, n):
        if j - i <= 7:
            if (a[i] + a[j]) % 8 != 0:
                count += 1
print(count)