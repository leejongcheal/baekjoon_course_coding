from collections import deque
INF = int(1e10)
steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M, K = map(int, input().split())
visit = [[INF] * M for _ in range(N)]
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))
q = deque()
# x y wall dis
q.append((0, 0, 0, 1))
visit[0][0] = 0
res = -1
while q:
    x, y, wall, dis = q.popleft()
    if x == N - 1 and y == M - 1:
        res = dis
        break
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0 and visit[nx][ny] > wall:
                q.append((nx, ny, wall, dis + 1))
                visit[nx][ny] = wall
            elif graph[nx][ny] == 1 and wall + 1 <= K and visit[nx][ny] > wall + 1:
                if dis % 2 == 1:
                    q.append((nx, ny, wall + 1, dis + 1))
                    visit[nx][ny] = wall + 1
                else:
                    # 벽벽이라서 2초후에 뚫고 가야하는 경우
                    # 또는 낮에 도착했는데 무조건 벽을 뚫고 가야하는 경우 고려
                    q.append((x, y, wall, dis + 1))
print(res)