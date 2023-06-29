a = [int(i) for i in open('17_2013.txt')]

b = []

for i in a:
    if i % 3 == 0 and i % 11 == 0 and (i % 10 == 2 or i % 10 == 7):
        b.append(i)

print(len(b), min(b))