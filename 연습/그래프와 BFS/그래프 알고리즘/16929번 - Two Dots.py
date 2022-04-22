steps = [(-1 ,0),(1, 0),(0, -1),(0, 1)]
def dfs(x, y,tracked):
    if visit[x][y] == 1:
        return 1
    if (x, y) in tracked:
        index = tracked.index((x, y))
        if len(tracked[index:]) >= 4:
            return 0
        else:
            return 1
    tracked.append((x, y))
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if Map[nx][ny] == Map[x][y]:
                if dfs(nx, ny, tracked) == 0:
                    return 0
    visit[x][y] = 1
    tracked.pop()
    return 1


N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
flag = 0
for i in range(N):
    for j in range(M):
        if visit[i][j] == 0:
            if dfs(i, j,[]) == 0:
                flag = 1
                break
    if flag:
        break
if flag:
    print("Yes")
else:
    print("No")