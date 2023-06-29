a = [int(i) for i in open('17_2239.txt')]

b = []
mx = max(i for i in a if abs(i) % 19 == 0)

for i in range(len(a) - 1):
    if a[i] > mx or a[i+1] > mx:
        b.append(a[i] + a[i+1])
print(len(b), min(b))