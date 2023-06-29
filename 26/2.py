with open('26_838.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
a.sort()
b = []
c = []

while len(a)!=0:
    b.append(a.pop(-1))
    while len(a)!=0 and sum(b) > sum(c):
        c.append(a.pop(0))

print(len(b), len(c))