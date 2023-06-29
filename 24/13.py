with open('24_2427.txt') as f:
    s = f.readline()

mx = r = s[0]
for i in range(1, len(s)):
    if s[i -1] > s[i]:
        r += s[i]
        mx = max(mx, r, key=len)
    else:
        r = s[i]
print(mx)