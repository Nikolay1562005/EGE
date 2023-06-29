with open('24_2423.txt') as f:
    s = f.readline()

mx = 0
r = 1
for i in range(len(s) - 1):
    if s[i] < s[i+1]:
        r += 1
    else:
        mx = max(mx, r)
        r = 1
print(mx)