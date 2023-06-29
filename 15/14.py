a = set()
b = {1, 3, 5, 7, 9, 11}
c = {3, 6, 9, 12}
def f(x):
    A = x in a
    B = x in b
    C = x in c
    return (B <= (not(C))) or A


for x in range(1000):
    if f(x) == 0:
        a.add(x)
print(sum(a))