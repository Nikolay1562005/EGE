with open('24_2426.txt') as f:
    s = f.readline()
s = s.replace('A', ' ').replace('B', ' ').replace('C', ' ').replace('  ', ' ').replace('  ', ' ').split()
print(max(len(i) for i in s))