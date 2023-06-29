with open('27B_2721.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

count = 0
k, k5, k13, k65 = 0, 0, 0, 0

for i in a:
    if i % 65 == 0: count += k
    elif i % 13 == 0: count += k5
    elif i % 5 == 0: count += k13
    else: count += k65
    k += 1
    if i % 65 == 0: k65 += 1
    if i % 13 == 0: k13 += 1
    if i % 5 == 0: k5 += 1

print(count)