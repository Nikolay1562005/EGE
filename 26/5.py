from itertools import combinations
with open('26_1257.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

a.sort()
a = set(a)
ans = []
for i in combinations(a, 2):
    if i[0]%2 != i[1]%2:
        sm = sum(i)
        if sm in a:
            ans.append(sm)

print(len(ans), max(ans))