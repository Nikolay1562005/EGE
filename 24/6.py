with open('24_1040.txt') as f:
    s = list(f.readline())

a = '0123456789'
for i in range(len(s)):
    if s[i] not in a:
        s[i] = ' '
s = ''.join(s)
for i in range(10):
    s = s.replace('  ', ' ')
s = s.split(' ')
print(max(len(i) for i in s))