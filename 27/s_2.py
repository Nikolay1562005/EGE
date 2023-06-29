with open('27B_2901.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

count = 0
s = [0]*666
k = 0
for i in a:
    k += i
    if k % 666 == 0: count += 1
    count += s[k % 666]

    s[k%666] += 1

print(count)