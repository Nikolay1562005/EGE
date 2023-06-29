with open('26_936.txt') as f:
    n, s = map(int, f.readline().split(' '))
    a = [int(i) for i in f]

a.sort(reverse=True)

k = 0
b = []

while len(a) != 0:
    b.clear()
    while len(a) != 0 and sum(b) + a[0] <= s:
        b.append(a.pop(0))
    if len(a) == 0:
        k += 1
        break
    for i in range(len(a)):
        if sum(b) + a[i] <= s:
            b.append(a.pop(i))
            break
    if sum(b) <= s:
        k += 1

print(k, sum(b))