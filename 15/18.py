def Del(n,m):
    return n%m == 0

for a in range(1,1000):
   a_true= True
   for x in range(1,1000):
       if ((not(Del(x,a)))<=