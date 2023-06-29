a = [int(i) for i in open('17_2017.txt')]

b = []

for i in a:
    if i % 16 == 11 and i % 7 == 0 and i % 6 != 0 and i % 13 != 0 and i % 19 != 0:
        b.append(i)

print(sum(b), len(b))