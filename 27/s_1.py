with open('27B_2900.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

mx = float('-inf')
s = [float('inf')]*1000
k = 0
for i in a:
    k += i
    if k%1000 == 0: mx = max(mx, k)
    if s[k%1000] != float('inf'):
        p = k - s[k%1000]
        mx = max(mx, p)

    s[k%1000] = min(k, s[k%1000])
print(mx)