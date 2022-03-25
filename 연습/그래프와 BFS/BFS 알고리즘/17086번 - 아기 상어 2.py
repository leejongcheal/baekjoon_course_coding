from collections import deque
def bfs(x, y):
    q = deque()
    visit = [[0] * M for _ in range(N)]
    visit[x][y] = 1
    q.append((x,y,0))
    while q:
        x, y, dist = q.popleft()
        if Map[x][y] == 1:
            return dist
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append((nx, ny, dist + 1))


steps = [(-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0),(1, -1),(0, -1),(-1, -1)]
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
res = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == 0:
            res = max(res, bfs(i,j))
print(res)