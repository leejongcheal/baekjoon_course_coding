from collections import deque, defaultdict
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
idx = 2
# 섬 별로 id 주기
for i in range(N):
    for j in range(M):
        if Map[i][j] == 1:
            q = deque()
            q.append((i, j))
            Map[i][j] = idx
            while q:
                x, y = q.popleft()
                for dx, dy in steps:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == 1:
                        q.append((nx, ny))
                        Map[nx][ny] = idx
            idx += 1
# 섬별로 가능한 다리 구하기
check = defaultdict(int)
graph = defaultdict(int)
graph_list = defaultdict(set)
for i in range(N):
    for j in range(M):
        if Map[i][j] != 0 and check[Map[i][j]] == 0:
            a = Map[i][j]
            q = [(i, j)]
            while q:
                x, y = q.pop()
                for dx, dy in steps:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        if Map[nx][ny] == 0:
                            dist = 0
                            while 0 <= nx + dx < N and 0 <= ny + dy < M:
                                dist += 1
                                nx += dx
                                ny += dy
                                if Map[nx][ny] != 0:
                                    if Map[nx][ny] != a and dist >= 2:
                                        b = Map[nx][ny]
                                        graph_list[a-2].add(b-2)
                                        if graph[(a-2, b-2)] == 0 or graph[(a-2, b-2)] > dist:
                                            graph[(a-2,b-2)] = dist
                                    break
                        elif Map[nx][ny] == a and check[(nx ,ny)] == 0:
                            q.append((nx, ny))
                            check[(nx, ny)] = 1
# 연결가능한것중 최소 거리 구하기
res = INF = int(1e10)
idx -= 2
visit = [0]*idx
for start in range(idx):
    q = deque()
    q.append(([start], 0))
    while q:
        traced, dist = q.popleft()
        if len(traced) == idx:
            res = min(res, dist)
            continue
        for now in traced:
            for next in graph_list[now]:
                if next not in traced:
                    q.append((traced + [next], dist + graph[(now, next)]))
if res == INF:
    res = -1
print(res)