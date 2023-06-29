with open('24_2421.txt') as f:
    s = f.readline()
s = s.replace('D', ' ').replace('  ', ' ').replace('  ', ' ').split()
print(max(len(i) for i in s))