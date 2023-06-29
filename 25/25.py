from fnmatch import*
import time

t1=time.time()
for c1 in '0123456789':
    for c2 in'0123456789':
        a=int(f'23{c1}456{c2}89')
        if a%17==0:
            print(a,a//17)
t2=time.time()
print(t2-t1)
