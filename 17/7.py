a = [int(i) for i in open('17_1994.txt')]

b = []

for i in range(len(a) - 1):
    if a[i]*a[i + 1] >= 0 and abs(a[i] + a[i + 1]) % 7 == 0:
        b.append(a[i]*a[i + 1])
print(len(b), min(b))