a = [int(i) for i in open('17_1999.txt')]

b = []

for i in range(len(a) - 2):
    if (abs(a[i]) % 12 == 0 or abs(a[i + 1]) % 12 == 0 or abs(a[i + 2]) % 12 == 0) and abs(a[i]) % 3 == 0 and abs(a[i + 1]) % 3 == 0 and abs(a[i + 2]) % 3 == 0:
        b.append((a[i] + a[i + 1] + a[i + 2])//3)
print(len(b), min(b))