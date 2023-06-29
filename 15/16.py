a = set()
b = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
c = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
def f(x):
    A = x in a
    B = x in b
    C = x in c
    return (A <= B) and (C <= (not(A)))


for x in range(100000):
    if f(x) == 0:
        a.add(x)
print(len(a))