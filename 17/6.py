a = [int(i) for i in open('17_1993.txt')]

b = []

for i in range(len(a) - 1):
    if abs(a[i] + a[i+1]) % 3 == 0 and abs(a[i] + a[i+1]) % 6 != 0 and abs(a[i]*a[i+1]) % 10 == 8:
        b.append(a[i] + a[i+1])
print(len(b), max(b))