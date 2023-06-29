with open('27B_2902.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

count = 0
d = [0]*11
k = 0
for i in a:
    if i % 5 == 0: k += 1
    if k % 11 == 0: count += 1
    count += d[k % 11]

    d[k%11] += 1
print(count)