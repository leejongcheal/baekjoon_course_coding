from collections import defaultdict
from itertools import combinations
N, M = map(int, input().split())
crim = [i for i in range(1, N + 1)]
combi = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    combi[a].add(b)
res = 0
for comb in combinations(crim, 3):
    a, b, c = comb
    if b in combi[a] or c in combi[a] or c in combi[b]:
        continue
    res += 1
print(res)