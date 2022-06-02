def dfs(sx, sy, value):
    global res
    res = max(res, value)
    flag = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0:
                x, y = i, j
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        return
    now = Map[x][y]
    visit[x][y] = 1
    dfs(x, y, value + int(now))
    mem = set()
    for i in range(1, N):
        if x + i < N and visit[x+i][y] == 0:
            now += Map[x+i][y]
            visit[x+i][y] = 1
            mem.add((x+i, y))
            dfs(x+i, y, value + int(now))
        else:
            break
    now = Map[x][y]
    for i, j in mem:
        visit[i][j] = 0
    mem = set()
    for j in range(1, M):
        if y + j < M and visit[x][y+j] == 0:
            now += Map[x][y+j]
            visit[x][y+j] = 1
            mem.add((x, y+j))
            dfs(x, y+j, value + int(now))
        else:
            break
    for i, j in mem:
        visit[i][j] = 0
    visit[x][y] = 0
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
res = 0
dfs(-1, -1, 0)
print(res)