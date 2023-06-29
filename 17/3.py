a = [int(i) for i in open('17_2015.txt')]

b = []

for i in a:
    if (i % 10 == 5 or i % 10 == 7) and i % 9 != 0 and i % 11 != 0:
        b.append(i)

print(len(b), max(b) + min(b))