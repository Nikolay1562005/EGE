a = [int(i) for i in open('17_2310.txt')]

mx = max([i for i in a if abs(i) % 10 == 4])
mn = min([i for i in a if abs(i) % 10 == 4])
s = mx + mn

b = []
for i in range(len(a) -1):
    if (a[i] + a[i + 1]) < s:
        b.append(a[i] + a[i + 1])

print(len(b), max(b))