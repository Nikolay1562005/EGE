a = [int(i) for i in open('17_2003.txt')]

b = []

for i in a:
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        b.append(i)
print(len(b), max(b))