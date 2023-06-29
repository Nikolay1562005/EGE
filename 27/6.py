with open('27B_2724.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
'''
k=0
for i in range(n):
    for j in range(i+1, n):
        if (a[i] + a[j]) % 131 == 0:
            k += 1
print(k)'''
b = [0]*131
for i in a:
    b[i % 131] += 1

k = b[0]*(b[0]-1)//2
for i in range(1, 66):
    k += b[i] * b[131 - i]

print(k)