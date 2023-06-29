def f(a,b,c,m): # s - количество ходов m - количество ходов c - начальный ход
      if a+b >= 80: return c%2 == m%2
      elif c == m: return 0
      
      if a<b: h = [f(a+1,b,c+1,m),f(a+2,b,c+1,m),f(a*2,b,c+1,m)]
      if a>b: h = [f(a,b+1,c+1,m),f(a,b+2,c+1,m),f(a,b2,c+1,m)]

      return any(h) if (c+1)%2 == m%2 else all(h)# any - когда одно из условий верно
                                                 # all - когда все условия истины
a= []   
for b in range(1, 6):
    for m in range(1,7):
        if f(s,0,m) == 1:
            if m == 4:
                print(b,m)
                a.append(s)
            break
print(len(a))
