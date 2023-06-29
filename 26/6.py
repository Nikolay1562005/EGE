with open('26_2652.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
b = set(a)
k = max([a.count(i) for i in b])
print(len(b), k)