a = [int(i) for i in open('17_2401.txt')]

b = []

for i in range(len(a) - 1):
    if 50 <= (abs(a[i]) + abs(a[i+1])) <= 200:
        b.append([a[i], a[i + 1]])
print(len(b), min(min(i) for i in b))