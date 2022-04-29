from collections import defaultdict
from heapq import heappop, heappush
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
char = set()
for i in range(N):
    for j in range(M):
        if Map[i][j] != ".":
            char.add(Map[i][j])
char = list(char)
total = len(char)
char_num = dict()
graph = defaultdict(list)
indegree = defaultdict(int)
for idx in range(total):
    now = char[idx]
    now_index = []
    for i in range(N):
        for j in range(M):
            if Map[i][j] == now:
                now_index.append([i, j])
    now_index.sort()
    sx, ex = now_index[0][0], now_index[-1][0]
    now_index.sort(key=lambda x:x[1])
    sy, ey = now_index[0][1], now_index[-1][1]
    nexts = set()
    for x in range(sx, ex + 1):
        for y in range(sy, ey + 1):
            if Map[x][y] != now:
                nexts.add(Map[x][y])
    for next in nexts:
        graph[now].append(next)
        indegree[next] += 1
res = ""
q = []
for c in char:
    if indegree[c] == 0:
        heappush(q, c)
while q:
    now = heappop(q)
    res += now
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            heappush(q, next)
if len(res) != total:
    res = -1
print(res)