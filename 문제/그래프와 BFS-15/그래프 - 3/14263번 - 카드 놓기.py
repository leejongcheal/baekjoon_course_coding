from collections import deque, defaultdict
import heapq


def find(val):
    L = []
    for i in range(N):
        for j in range(M):
            if Map[i][j] == val:
                L.append([i, j])
    L.sort()
    n_list = [i for i in range(L[0][0], L[-1][0] + 1)]
    L.sort(key=lambda x: x[1])
    m_list = [i for i in range(L[0][1], L[-1][1] + 1)]
    group = set()
    for i in n_list:
        for j in m_list:
            group.add((i, j))
    return group


steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
groups = defaultdict(set)
for i in range(N):
    for j in range(M):
        if Map[i][j]!= "." and Map[i][j] not in groups.keys():
            groups[Map[i][j]] = find(Map[i][j])
indegree = defaultdict(int)
graph = defaultdict(list)
visit = []
flag = 0
for val in groups.keys():
    for x, y in groups[val]:
        if Map[x][y] != val and Map[x][y] not in graph[val]:
            graph[val].append(Map[x][y])
            indegree[Map[x][y]] += 1

q = []
res = ""
for key in groups.keys():
    if indegree[key] == 0:
        heapq.heappush(q,key)
while q:
    now = heapq.heappop(q)
    res += now
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            heapq.heappush(q, next)
for key in groups.keys():
    if key not in res:
        res = - 1
        break
if res != -1 and len(res) != len(groups):
    res = -1
print(res)