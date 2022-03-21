steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(x, y, now, cnt):
    global Max, L, N, M, Max_value
    if cnt == 4:
        Max = max(Max, now)
        return
    if (4 - cnt)*Max_value + now < Max:
        return
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
            if cnt == 2:
                visit[nx][ny] = 1
                dfs(x, y, now + L[nx][ny], cnt + 1)
                visit[nx][ny] = 0
            visit[nx][ny] = 1
            dfs(nx, ny, now + L[nx][ny], cnt + 1)
            visit[nx][ny] = 0


N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
Max_value = max([max(l) for l in L])
visit = [[0]*M for _ in range(N)]
Max = -int(1e10)
for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        dfs(i,j,L[i][j], 1)
        visit[i][j] = 0
print(Max)