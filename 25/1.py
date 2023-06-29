k = []
for i in range(174457, 174506):
    r = []
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            r.append(j)
            r.append(int(i/j))
    if len(r) == 2:
        k.append(r)
for i in k:
    i.sort()
    print(*i)