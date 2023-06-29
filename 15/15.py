a = set()
b = {3, 6, 9, 12}
c = {1, 2, 3, 4, 5, 6}
def f(x):
    A = x in a
    B = x in b
    C = x in c
    return (not((not(A)) and (B))) or (not(C))


for x in range(1000):
    if f(x) == 0:
        a.add(x)
print(len(a))