with open('27B_2758.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

mn = float('inf')

for i in range(n):
    for j in range(i + 1, n):
        if j - i <= 11:
            b = a[i] + a[j]
            if b % 2142 == 0:
                mn = min(mn, b)

print(mn)