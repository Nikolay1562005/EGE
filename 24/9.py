with open('24_1302.txt') as f:
    s = f.readline()
mx = 0
r = 3
for i in range(len(s) - 3):
    if s[i:i+4] == 'XZZY':
        mx = max(mx, r)
        r = 3
    else:
        r += 1
print(mx)