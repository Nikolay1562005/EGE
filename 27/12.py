with open('27B_2728.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

b_23 = sorted([i for i in a if i % 23 == 0])
b = sorted([i for i in a if i % 23 != 0])
k = 0
for i in range(0, -15, -1):
    for j in range(0, -15, -1):
        if (b_23[i] + b[j]) % 2 == 0:
            k = max(b_23[i] + b[j], k)
print(k)