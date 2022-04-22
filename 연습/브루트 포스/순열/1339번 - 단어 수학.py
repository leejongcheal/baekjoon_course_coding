from collections import defaultdict
num = defaultdict(int)
N = int(input())
L = list(list(input()) for _ in range(N))
for l in L:
    for idx, s in enumerate(l, 1):
        num[s] += 10**(len(l) - idx)
A = []
for s in num.keys():
    A.append(num[s])
A.sort(reverse=True)
res = 0
now = 9
for val in A:
    res += val*now
    now -= 1
print(res)