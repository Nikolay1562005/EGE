with open('24_1146.txt') as f:
    s = f.readline().strip()

for i in set(s):
    if i != 'D':
        s = s.replace(i, ' ')
s = s.replace(' D ', ' ').replace(' DD ', ' ').replace(' D', ' ').replace('D ', ' ')
mn = 10000
k = 0
for i in s:
    if i == 'D':
        k += 1
        mn = min(mn, k)
    else:
        k = 0
print(mn)