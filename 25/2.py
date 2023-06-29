def f(n):
    s = []
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            s.append(i)
            s.append(n//i)
    return set(s)

for i in range(81234, 134690):
    if len(f(i)) == 3:
        print(*sorted(list(f(i))))