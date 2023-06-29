with open('27B_2720.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
count = 0
k = 0
k7 = 0
for i in a:
    if i % 7 == 0: count += k
    else: count += k7
    k += 1
    if i % 7 == 0: k7 += 1

print(count)