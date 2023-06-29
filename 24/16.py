with open('24_2250.txt') as f:
    s = f.readline().strip()

s = s.split('A')
m = 0
for i in range(len(s) - 1):
    m = max(m, len(s[i] + 'A' + s[i+1]))
print(m)