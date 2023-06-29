from fnmatch import*
import time

def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x%i == 0:
            d|={i,x//i}
    return sorted(d)

t1=time.time()
for x in range(0,10**7,217):
    if fnmatch(str(x),'27?7*'):
            print(x,sum([i for i in div(x) if i%2 != 0]))
t2=time.time()
print(t2-t1)
