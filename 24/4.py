with open('24_865.txt') as f:
    s = f.readline()
s = s.replace('C', ' ').replace('F', ' ').replace('  ', ' ').replace('  ', ' ').split()
print(max(len(i) for i in s))