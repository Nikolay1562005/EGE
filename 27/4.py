with open('27B_2722.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
'''
k = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i]*a[j] % 5 == 0 and (a[i] + a[j]) % 2 == 1:
            k += 1
print(k)'''

a_5 = [i for i in a if i % 5 == 0]

a_5_1 = [i for i in a_5 if i % 2 == 1]
a_5_0 = [i for i in a_5 if i % 2 == 0]

a_1 = [i for i in a if i % 2 == 1 and i not in a_5_1]
a_0 = [i for i in a if i % 2 == 0 and i not in a_5_0]

print(len(a_5_1)*len(a_5_0) + len(a_5_1)*len(a_0) + len(a_5_0)*len(a_1))