a = [int(i) for i in open('17_2238.txt')]

b = []
sa = sum(a)/len(a)
for i in range(len(a) - 2):
    if (int(a[i] > sa) + int(a[i+1] > sa) + int(a[i+2] > sa)) > 1:
        b.append(a[i] + a[i+1] + a[i+2])
print(len(b), max(b))