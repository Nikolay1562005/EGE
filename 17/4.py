a = [int(i) for i in open('17_2016.txt')]

b = []

for i in a:
    if i % 13 == 7 and i % 7 != 0 and i % 11 != 0:
        b.append(i)

print(max(b) - min(b), len(b))