with open('24_1975.txt') as f:
    s = f.readline()
s = s.replace('PP', 'P P')
for i in range(10):
    s = s.replace('PP', 'P')
s = s.split(' ')
print(max(len(i) for i in s))