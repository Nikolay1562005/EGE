with open('27A_2733.txt') as f:
    n = int(f.readline())
    s = [int(i) for i in f]

count = 0
k = [0]*80
k_50_000 = [0]*80

for i in s:
    ost = i % 80
    if i <= 50_000:
        count += k_50_000[(80 - ost) % 80]
    else:
        count += k[(80 - ost) % 80] + k_50_000[(80 - ost) % 80]

    if i <= 50_000: k[ost] += 1
    else: k_50_000[ost] += 1

print(count)