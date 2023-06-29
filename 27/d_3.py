with open('27B_2722.tx') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

count = 0
k_1, k_0, k_5_1, k_5_0 = 0, 0, 0, 0

for i in a:
    if i%2 == 1:
        if i%5 == 0: count += k_0
        else: count += k_5_0
    else:
        if i%5 == 0: count += k_1
        else: count += k_5_1

    if i%2 == 1:
        if i%5 == 0:
            k_5_1 += 1
            k_1 += 1
        else: k_1 += 1
    else:
        if i%5 == 0:
            k_5_0 += 1
            k_0 += 1
        else: k_0 += 1

print(count)