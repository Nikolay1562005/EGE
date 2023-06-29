from fnmatch import*
import time

t1=time.time()
print(t1/(365*24*60*60))
for x in range(4294967237,10**10,121):
    if fnmatch(hex(x)[2:],f'1?ded?ced'):
            print(x,x//121)
t2=time.time()
print(t2-t1)
            

b=[]
for c1 in '0123456789abcdef':
    for c2 in '0123456789abcdef':
        a=int(f'1{c1}ded{c2}ced',16)
        if a%121 == 0:
            b+= [(a,a//121)]

for x in b[::-1]:
    print(*x)
t3=time.time()
print(t3-t2)
