from math import *
with open('27B_2723.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
a_19 = len([i for i in a if i % 19 == 0])
print(a_19)
print((factorial(a_19))//(factorial(3)*factorial(a_19-3)))