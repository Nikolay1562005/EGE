with open('27B_2737.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

k=0
for i in range(n):
    for j in range(i+1, n):
        if a[i] + a[j] == 2_000:
            k += 1
print(k, len(a))