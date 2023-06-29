with open('24_2420.txt') as f:
    s = f.readline()
s = s.replace('C', ' ').replace('D', ' ').replace('  ', ' ').replace('  ', ' ').split()
print(max(len(i) for i in s))