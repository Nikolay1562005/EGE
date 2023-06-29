with open('27B_2760.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

mn = float('inf')

for i in range(n):
    for j in range(i, n, 5):
        if i != j and (a[i] + a[j])%107 == 0:
            mn = min(mn, a[i] + a[j])
print(mn)