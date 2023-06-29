with open('24_1145.txt') as f:
    s = f.readline()

s = s.replace('D', 'D D').replace('DD', ' ')
s = s.split()
print(len(min(s, key=len)))