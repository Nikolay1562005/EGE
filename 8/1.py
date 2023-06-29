import itertools

k = 0
for i in itertools.product("КРСЛ", "КРЕСЛО", "КРЕСЛО", "ЕО"):
    k += 1
print(k)