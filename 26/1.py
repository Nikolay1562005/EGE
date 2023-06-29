with open('26_813.txt') as f:
    a, b = map(int, f.readline().split(' '))
    s = [int(i) for i in f]

s.sort()
d = []

while sum(d) <= a:
    if (sum(d) + s[-1]) <= a:
        d.append(s.pop(-1))
    else: break
    if (sum(d) + s[0]) <= a:
        d.append(s.pop(0))
    else: break

print(len(d), d[-1], sum(d), a)
print(d)