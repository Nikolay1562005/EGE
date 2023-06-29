with open('27B_6318.txt') as f:
    n, m = map(int, f.readline().split(' '))
    a = [int(i) for i in f]

s = mx = sum(a[:2*m+1])

for i in range(m + 1, n - m):
    s += a[i + m] - a[i - m - 1]
    mx = max(mx, s)

print(mx)