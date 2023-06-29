from itertools import combinations
with open('27B_7603.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
a0 = [x for x in a if x % 2 == 0]
a1 = [x for x in a if x % 2 == 1]
print(len(a0))
k = (len(a0)*(len(a0)-1))/2
print(len(a1))
k += (len(a1)*(len(a1)-1))/2
print(k)