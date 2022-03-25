from collections import deque


def bfs(x, y):
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] == Map[x][y] and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append((nx, ny))


N = int(input())
Map = [list(input()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
a, b = 0, 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            a += 1
            bfs(i, j)
for i in range(N):
    for j in range(N):
        if Map[i][j] == "G":
            Map[i][j] = "R"
visit = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            b += 1
            bfs(i, j)
print(a, b)
