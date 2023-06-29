k = 0
for i in range(1, 1000):
    if i < 5**4 and i >= 2**4 and i%16 == 12:
        k += 1
print(k)