with open('27B_2720.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
'''
k = 0
for i in range(n):
    for j in range(i + 1, n):
        if (a[i]*a[j]) % 7 == 0:
            k += 1
print(k)
'''
a_7 = [x for x in a if x % 7 == 0]
a_not7 = [x for x in a if x % 7 != 0]

print(len(a_7)*len(a_not7) + (len(a_7)*(len(a_7)-1))//2)