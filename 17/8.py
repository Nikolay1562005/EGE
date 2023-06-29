a = [int(i) for i in open('17_1998.txt')]

b = []

for i in range(len(a) - 2):
    if abs(a[i]*a[i + 1]*a[i + 2]) % 7 == 0 and abs(a[i] + a[i + 1] + a[i + 2]) % 10 == 5:
        b.append(a[i] + a[i + 1] + a[i + 2])
print(len(b), max(b))