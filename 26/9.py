with open('26_2651.txt') as f:
    n = int(f.readline())
    a = [[int(i.split(' ')[0]), int(i.split(' ')[1])] for i in f]

b ={}
for i in range(1961, 1991 + 1):
    b[i] = []
for x, y in a:
    b[x].append(y)

k = 0
date = [[]]
for i in b:
    j = b[i]
    count_type = 0
    for l in range(1, 8 + 1):
        if j.count(l) > 0:
            count_type += 1
    if count_type != 8:
        k += 8-count_type
        date.append([8-count_type, i])
date.sort(reverse=True)
print(k, date[0][1])