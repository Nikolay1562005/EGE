from random import *
a = [randint(2, 1000000) for i in range(1_000_000)]

n =len(a)
k = 1000
mB = float('inf')
m = [float('inf')]*n
m2 = [float('inf')]*n
for i in range(k, n):
    m[i - k] = min(m[i - k - 1], a[i - k])
    m2[i] = min(m2[i - 1], m[i - k]*a[i])
    mB = min(mB, a[i]*m2[i - k])
print(mB)