def f(a,b,c,m): # s - количество ходов m - количество ходов c - начальный ход
      if a + b <= 20: return c%2 == m%2
      elif c == m: return 0
      h = [f(a-1, b, c+1, m), f(a, b-1, c+1, m),f((a+1)//2, b, c+1, m),f(a, (b+1)//2, c+1, m),]
      return any(h) if (c+1)%2 == m%2 else all(h)# any - когда одно из условий верно
                                                 # all - когда все условия истины
    
for b in range(11, 200):
    for m in range(1,5):
        if f(10,b,0,m) == 1:
            print(b,m)
            break
