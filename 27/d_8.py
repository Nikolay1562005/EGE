with open('27B_2728.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

k = [float('-inf'), float('-inf')]
k_23 = [float('-inf'), float('-inf')]
mx = float('-inf')

for i in a:
    if i%23 == 0:
        mx = max(mx, k[int(i % 2 == 1)] + i,  k_23[int(i % 2 == 1)] + i)
    else:
        mx = max(mx, k_23[int(i % 2 == 1)] + i)

    if i%23 == 0:
        k_23[i % 2] = max(k_23[i % 2], i)
    else:
        k[i % 2] = max(k[i % 2], i)
print(mx)