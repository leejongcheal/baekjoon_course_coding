from collections import defaultdict
N, M = map(int, input().split())
friend = defaultdict(list)
visit = defaultdict(int)
for _ in range(M):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
INF = res = int(1e10)
r = set()
cnt = 0
ccnt = 0
for a in range(1, N + 1):
    for b in friend[a]:
        if visit[(a, b)] == 0:
            visit[(a, b)] = visit[(b, a)] = 1
            for c in friend[b]:
                ccnt += 1
                if c in friend[a]:
                    res = min(res, len(friend[a]) + len(friend[b]) + len(friend[c]) - 6)
if res == INF:
    res = -1
print(res)