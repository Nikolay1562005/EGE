from fnmatch import*
import time

t1=time.time()
for x in range(0,10**9,17):
    if fnmatch(str(x),'23?456?89'):
            print(x,x//17)
t2=time.time()
print(t2-t1)
