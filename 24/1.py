with open('24_2419.txt') as f:
    s = f.readline()
s = s.replace('A', ' ').replace('B', ' ').replace('  ', ' ').replace('  ', ' ').split()
print(max(len(i) for i in s))