a = [int(i) for i in open('17_2309.txt')]

b_11 = []
b_17 = []

for i in a:
    if i % 11 == 0:
        b_11.append(i)
    if i % 17 == 0:
        b_17.append(i)
if len(b_11) > len(b_17):
    print(len(b_11), min(b_11))
else:
    print(len(b_17), max(b_17))