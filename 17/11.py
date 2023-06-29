a = [int(i) for i in open('17_2002.txt')]

b = []

for i in range(len(a) - 3):
    if a[i] >= a[i + 1] >= a[i + 2] >= a[i + 3] and a[i] - a[i + 3] > 1000:
        b.append(a[i] + a[i+1] + a[i+2] + a[i+3])
print(len(b), min(b))