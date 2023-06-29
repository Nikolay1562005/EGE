from itertools import combinations
with open('26_1079.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
a.sort()
ans = []
for i in combinations(a, 2):
    i = sum(i)
    if i % 2 == 0:
        sr = i//2
        if a[n//2-1] < sr < a[(n//4)*3]:
            ans.append(sr)
print(len(ans), min(ans))