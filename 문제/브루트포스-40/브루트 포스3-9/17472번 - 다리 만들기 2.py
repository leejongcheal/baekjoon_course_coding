from collections import deque, defaultdict
from copy import deepcopy
def island_number(x, y):
    global island_cnt
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == 1 and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            Map[nx][ny] = island_cnt
            group.append((nx, ny))
            island_number(nx, ny)
def make_graph():
    for island in range(island_cnt):
        for x, y in island_group[island]:
            for dx, dy in steps:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == 0:
                    d = 1
                    flag = 0
                    while 1:
                        nx += dx
                        ny += dy
                        if not (0 <= nx < N and 0 <= ny < M):
                            break
                        elif Map[nx][ny] != 0:
                            flag = 1
                            break
                        d += 1
                    if flag and d >= 2:
                        a, b = island, Map[nx][ny] - 1
                        graph[a][b] = min(graph[a][b], d)
                        graph[b][a] = min(graph[b][a], d)

INF = int(1e10)
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
island_cnt = 1
island_group = []
visit = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visit[i][j] == 0 and Map[i][j] != 0:
            visit[i][j] = 1
            Map[i][j] = island_cnt
            group = [(i, j)]
            island_number(i, j)
            island_cnt += 1
            island_group.append(group)
island_cnt -= 1
graph = [[INF]*island_cnt for _ in range(island_cnt)]
make_graph()
res = INF
q = deque()
q.append(([0], 0))

while q:
    tracked, dist = q.popleft()
    if len(tracked) == island_cnt:
        res = min(res, dist)
        continue
    for now in tracked:
        for next in range(island_cnt):
            if graph[now][next] != INF and next not in tracked:
                q.append((tracked+[next], dist + graph[now][next]))
if res != INF:
    print(res)
else:
    print(-1)


