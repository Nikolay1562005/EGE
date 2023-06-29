with open('27B_2719.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
a_0 = [x for x in a if x % 2 == 0]
a_1 = [x for x in a if x % 2 == 1]

k = (len(a_0) * (len(a_0) - 1))//2 + (len(a_1) * (len(a_1) - 1))//2
print(k)