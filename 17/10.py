a = [int(i) for i in open('17_2402.txt')]

b = []

for i in range(len(a) - 2):
    if a[i] % 3 == 2 or a[i + 1] % 3 == 2 or a[i + 2] % 3 == 2:
        b.append(min(a[i], a[i + 1], a[i + 2]))
print(len(b), sum(b))