from fnmatch import *

for i in range(10**6):
    if fnmatch(str(i), '1*2*6'):
        print(i)