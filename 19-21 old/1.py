def f(s,c,m): # s - количество ходов m - количество ходов c - начальный ход
      if s >= 30: return c%2 == m%2
      elif c == m: return 0
      h = [f(s+2, c+1, m), f(s+3, c+1, m), f(s*2, c+1, m)]
      return any(h) if (c+1)%2 == m%2 else all(h)# any - когда одно из условий верно
                                                 # all - когда все условия истины
    
for s in range(1,30):
    for m in range(1,5):
        if f(s,0,m) == 1:
            print(s,m)
            break
