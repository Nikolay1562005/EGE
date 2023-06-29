from bisect import *
with open('26_2650.txt') as f:
    l, m, n = map(int, f.readline().split(' '))
    a = [[int(i.split(' ')[0]), int(i.split(' ')[1])+int(i.split(' ')[0])+m+1] for i in f]
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
x = []
end = 0
for i in b:
    x.append([end, i[0]])
    end = i[1] - m - 1
x.append([end, l])
print(x)
print(len(x), max([i[1]-i[0] for i in x]))