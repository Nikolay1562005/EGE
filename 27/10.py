with open('27B_2726.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

k_0 = max([i for i in a if i % 2 == 0])
k_1 = max([i for i in a if i % 2 == 1])
print(k_0 + k_1)