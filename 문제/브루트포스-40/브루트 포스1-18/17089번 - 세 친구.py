from collections import defaultdict
from itertools import combinations


INF = int(1e10)
res = INF
N, M = map(int, input().split())
friend = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    friend[a].add(b)
    friend[b].add(a)
L = []
for i in range(1, N + 1):
    if len(friend[i]) != 0:
        L.append(i)
for comb in combinations(L, 3):
    a, b, c = comb
    if b in friend[a] and c in friend[a] and c in friend[b]:
        val = len(friend[a]) + len(friend[b]) + len(friend[c]) - 6
        res = min(res, val)
if res == INF:
    print(-1)
else:
    print(res)