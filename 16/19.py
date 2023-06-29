def f(n):
    if n <= 1: return n
    else:
        if n%3 == 0: return f(n//3) + n
        else: return f(n+3) + n


for i in range(1, 1000):
    try:
        if f(i) > 100:
            print(i)
            break
    except:
        pass