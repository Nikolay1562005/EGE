with open('27B_2733.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
'''
k=0
for i in range(n):
    for j in range(i+1, n):
        if (a[i] + a[j]) % 80 == 0 and (a[i] > 50_000 or a[j] > 50_000):
            k += 1
print(k)'''
b_50_000 = [0]*80
b = [0]*80
for i in a:
    if i > 50_000:
        b_50_000[i % 80] += 1
    else:
        b[i % 80] += 1

k = b_50_000[0]*(b_50_000[0] - 1)//2 + b_50_000[40]*(b_50_000[40] - 1)//2
for i in range(1, 40):
    k += b_50_000[i]*b_50_000[80 - i]
k += b_50_000[0]*b[0] + b_50_000[40]*b[40]
for i in range(1, 40):
    k += b_50_000[i]*b[80-i]
    k += b[i]*b_50_000[80 - i]

print(k)