def dfs(x, y):
    global cnt
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0 and Map[nx][ny] == "0":
            visit[nx][ny] = 1
            cnt += 1
            dfs(nx, ny)


steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
N, M = map(int, input().split())
visit = [[0]*M for _ in range(N)]
res = [["0"]*M for _ in range(N)]
Map = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if Map[i][j] == "1":
            Map[i][j] = "0"
            cnt = 1
            visit = [[0]*M for _ in range(N)]
            visit[i][j] = 1
            dfs(i, j)
            res[i][j] = str(cnt)
            Map[i][j] = "1"
for r in res:
    print("".join(r))


