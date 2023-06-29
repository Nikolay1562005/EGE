with open('26_2480.txt') as f:
    n = int(f.readline())
    a = [[int(i.split(' ')[0]), int(i.split(' ')[1])] for i in f]
a.sort()
b = [a[0]]
for c, d in a:
    for i in range(len(b)):
        h, g = b[i][0], b[i][1]
        if h <= c <= g and h <= d <= g:
            break
        if h <= c <= g or h <= d <= g or (c <= h and g <= d):
            b[i][0], b[i][1] = min(c, d, h, g), max(c, d, h, g)
            break
    else:
        b.append([c, d])
print(len(b), sum([i[1]-i[0] for i in b])) # 1912 949174