with open('24_1428.txt') as f:
    s = f.readline()

s = s.replace('XY', 'X Y').replace('XZ', 'X Z')
s = s.split(' ')
print(max(len(i) for i in s))