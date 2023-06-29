k = []

for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            if a <= b and b <= c:
                k.append(100*a + 10*b + c)

print(len(k))