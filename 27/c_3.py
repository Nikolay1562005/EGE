with open('27B_4116.txt') as f:
    n, k = map(int, f.readline().split(' '))
    a = [int(i) for i in f]

s = a[0]
mx = st = end = 0
while s + a[end + 1] <= k:
    s += a[end + 1]
    end += 1


while end != n - 1:
    s -= a[st]
    st += 1
    while end != n - 1 and s + a[end + 1] <= k:
        s += a[end + 1]
        end += 1
    mx = max(mx, end - st + 1)

print(mx)

mx = 0
for i in range(n):
    s = k0 = 0
    for j in range(i, n):
        s += a[j]
        if s <= k:
            k0 += 1
            mx = max(k0, mx)
        else: break
print(mx)