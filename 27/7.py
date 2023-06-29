with open('27B_2725.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
'''
k=0
for i in range(n):
    for j in range(i+1, n):
        if (a[i] - a[j]) % 69 == 0:
            k += 1
print(k)'''

b = [0]*69
for i in a:
    b[i % 69] += 1

k = 0
for i in range(0, 69):
    k += b[i]*(b[i]-1)//2
print(k)