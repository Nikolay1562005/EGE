def f(s,c,m): # s - количество ходов m - количество ходов c - начальный ход
      if s >= 51: return c%2 == m%2
      elif c == m: return 0
      if s%2 == 0: h=[f(s+1,c+1,m),f(s+3,c+1,m)]
      else: h = [f(s*3,c+1,m)]
      return any(h) if (c+1)%2 == m%2 else all(h)# any - когда одно из условий верно
                                                 # all - когда все условия истины
a= []   
for s in range(1, 51):
    for m in range(1,7):
        if f(s,0,m) == 1:
            if m == 4:
                print(s,m)
                a.append(s)
            break
print(len(a))
