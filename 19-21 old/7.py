def f(s,c,m): # s - количество ходов m - количество ходов c - начальный ход
      if s >= 22: return c%2 == m%2
      elif c == m: return 0
      h = [f(s+1,c+1,m), f(s+2,c+1,m)]
      if s%2 == 1: h+=[f(s*2,c+1,m)]
      return any(h) if (c+1)%2 == m%2 else all(h)# any - когда одно из условий верно
                                                 # all - когда все условия истины
    
for s in range(1, 22):
    for m in range(1,7):
        if f(s,0,m) == 1:
            print(s,m)
            break
