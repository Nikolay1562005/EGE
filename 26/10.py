from tqdm import tqdm
from alive_progress import alive_bar
with open('26_2653.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
a.sort()
weight = [0]*(sum(a)+1)
with alive_bar(n) as bar:
    for i in range(n):
        bar()
        weight2 = weight.copy()
        for j in range(len(weight)):
            if weight[j] > 0:
                weight2[j+a[i]] += weight[j]
        weight2[a[i]] += 1
        weight = weight2
mx = 0
for i in range(len(weight)-1, 1, -1):
    if weight[i] == 0:
        mx = i
        break
print(weight.count(0)-1, mx)